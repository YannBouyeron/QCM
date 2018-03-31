import json
from bottle import *
import random


#importation des qcm
with open('qcm.txt', 'r') as fp:
	
	qcm = json.load(fp)




#fonction case automatique
def case(action, method, txt, value, **name):

		x = " ".join(["""<input type="checkbox" name="{n}" value="{m} id="{n}" /> <label for="{n}">{m}</label><br/>""".format(n = i, m = name[i]) for i in name.keys()])
	
		return """<form action="{0}" method="{1}"> {2} <br/> {3} <input value="{4}" type="submit" /> </form>""".format(action, method, txt, x, value)





app = Bottle()



@app.route('/')
def index():
	
	#recherche du cookie avec l'historique des questions traitées
	hist = request.get_cookie("hist", secret="1234")
	
	#choix d'une question
	question = random.choice(qcm)
	x = qcm.index(question)
	
	if hist != None:
		while x in hist:
			question = random.choice(qcm)
			x = qcm.index(question)
	
	#ajout de x à l'historique et envoi du cookie
	if hist == None:
		hist = []
	hist.append(x)
	
	response.set_cookie("hist", hist, secret="1234")
			
	#construction du html
	htmlqcm = case('/traite', 'post', question[0], 'Valider', **question[1])
	
	return template('index.html', x = htmlqcm)
	
	
@app.post('/traite')
def traitement():
	
	#recup indice question
	hist = request.get_cookie("hist", secret="1234")
	x = hist[-1]
	
	#recup cookie_result
	z = request.get_cookie("result", secret="1234")
	
	
	#recup bonnes reponses
	g = qcm[x][2]
	
	#recup choix reponses
	c = qcm[x][1]
	
	#recup reponse candidat
	r = []
	for i in c:
		if request.forms.get(i):
			r.append(int(i))
	
	g.sort()
	r.sort()
	
	#si la ou les reponses sont bonnes
	if g == r:
		
		#on ajoute un "g" à z
		if z == None:
			z = 'g'
		
		else: 
			z = z + 'g'
		
		#envoi cookie resulte... on ne dispose que de 15 minutes pour repondre a la question suivante
		response.set_cookie("result", z, secret="1234", max_age=900)
		
	#si au moins l'une des réponses est fausse
	else:
		
		#on ajoute un "b" à z
		if z == None:	
			z = 'b'
		
		else: 
			z = z + 'b'
		
		#envoi cookie resulte... on ne dispose que de 15 minutes pour repondre a la question suivante
		response.set_cookie("result", z, secret="1234", max_age=900)
	
	
	#si on a pas encore repondu a toute les questions... on recommence... il faut répondre à 5 questions 
	if len(z) < 4:
		
		response.status = 303
		response.set_header('Location', '/')
		
	#sinon et si il n'y a pas de "b" dans z, on à gagné	
	elif 'b' not in z:
		
		#on suprime le cookie result
		response.set_cookie("result", 'fin', secret="1234", max_age=0)
		response.set_cookie("hist", 'fin', secret="1234", max_age=0)
		return 'gagné'
		
	#sinon on a perdu	
	else:
		
		#on supprime le cookie result
		response.set_cookie("result", 'fin', secret="1234",max_age=0)
		response.set_cookie("hist", 'fin', secret="1234", max_age=0)
		return 'perdu'
	
	
app.run(host='0.0.0.0', port=27200, reload=True, debug=True)
