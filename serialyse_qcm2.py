import json

qcm = [['un gabbro est', {1:'une roche métamorphique', 2:'une roche magmatique', 3:'une roche sédimentaire', 4:'une roche grenue'},[2, 4]],['richard stallman est', {1:'un genie', 2:'cool', 3:'le père noel', 4:'plus fort que bill gats'}, [1,2,3,4]],['la croute continentale est composée de', {1:'basaltes', 2:'granitoides', 3:'péridotites', 4:'gabbros'}, [2]], ['la distance terre - soleil est de', {1:'150 milliards de km', 2:'150 km', 3:'150 millions de km', 4:'15 millions de km'}, [3]], ['Dakar est situé à une latitude de', {1:'+ 15°', 2:'+ 30°', 3:'- 15°', 4:'- 30°'}, [1]]]

x = json.dumps(qcm, ensure_ascii=False, indent=4)

with open('qcm.txt', 'wb') as fp:
	
	fp.write(x.encode())
	

with open('qcm.txt', 'rb') as fp:
	
	y = fp.read().decode()
	
h = json.loads(y)
