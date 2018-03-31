# QCM

Créer vos QCM en ligne avec bottle et python.

## Création d'un QCM

pour ajouter une question, modifiez "manuellement" le fichier qcm.txt, ou utilisez le script python serialyse_qcm2.py .

Chaque question de QCM est une liste : ["énoncé de la question", {1:"reponse 1", 2:"reponse 2", 3:"reponse 3", 4:"reponse 4"}, [2,3]]

Chaque liste contient 3 éléments:

- une str: l'énomncé de la question
- un dictionnaire dont les clés sont les index des reponses, et les valeurs sont les réponses
- une liste contenant les index des bonnes réponses

## Lancement de l'application en local

Placez vous dans le repertoire de l'application, et exécutez le script qcmhtml.py:

	python3 qcmhtml.py 
