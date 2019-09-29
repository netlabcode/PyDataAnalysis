
import csv
import datetime

FreqData = open('Output.csv')
ReadFreqCSV = csv.DictReader(FreqData, delimiter=',')

newRecord = []
Zoneentifier=1


#create empty variable of Day 1-96 ==============================
for n in range(0, 97):
	globals()['Monday%s' % n] = 0


for n in range(0, 97):
	globals()['Tuesday%s' % n] = 0

for n in range(0, 97):
	globals()['Wednesday%s' % n] = 0

for n in range(0, 97):
	globals()['Thursday%s' % n] = 0

for n in range(0, 97):
	globals()['Friday%s' % n] = 0

for n in range(0, 97):
	globals()['Saturday%s' % n] = 0

for n in range(0, 97):
	globals()['Sunday%s' % n] = 0




for row in ReadFreqCSV:
	############## MONDAY HERE ##################
	if "Monday" in row["Day"]:
		
		if row["Zone"] == "1":
			Monday1 = Monday1+1
		elif row["Zone"] == "2":
			Monday2 = Monday2+1
		elif row["Zone"] == "3":
			Monday3 = Monday3+1
		elif row["Zone"] == "4":
			Monday4 = Monday4+1
		elif row["Zone"] == "5":
			Monday5 = Monday5+1
		elif row["Zone"] == "6":
			Monday6 = Monday6+1
		elif row["Zone"] == "7":
			Monday7 = Monday7+1
		elif row["Zone"] == "8":
			Monday8 = Monday8+1
		elif row["Zone"] == "9":
			Monday9 = Monday9+1
		elif row["Zone"] == "10":
			Monday10 = Monday10+1

		elif row["Zone"] == "11":
			Monday11 = Monday11+1
		elif row["Zone"] == "12":
			Monday12 = Monday12+1
		elif row["Zone"] == "13":
			Monday13 = Monday13+1
		elif row["Zone"] == "14":
			Monday14 = Monday14+1
		elif row["Zone"] == "15":
			Monday15 = Monday15+1
		elif row["Zone"] == "16":
			Monday16 = Monday16+1
		elif row["Zone"] == "17":
			Monday17 = Monday17+1
		elif row["Zone"] == "18":
			Monday18 = Monday18+1
		elif row["Zone"] == "19":
			Monday19 = Monday19+1
		elif row["Zone"] == "20":
			Monday20 = Monday20+1


		elif row["Zone"] == "21":
			Monday21 = Monday21+1
		elif row["Zone"] == "22":
			Monday2 = Monday2+1
		elif row["Zone"] == "23":
			Monday23 = Monday23+1
		elif row["Zone"] == "24":
			Monday24 = Monday24+1
		elif row["Zone"] == "25":
			Monday25 = Monday25+1
		elif row["Zone"] == "26":
			Monday26 = Monday26+1
		elif row["Zone"] == "27":
			Monday27 = Monday27+1
		elif row["Zone"] == "28":
			Monday28 = Monday28+1
		elif row["Zone"] == "29":
			Monday29 = Monday29+1
		elif row["Zone"] == "10":
			Monday30 = Monday30+1

		elif row["Zone"] == "31":
			Monday31 = Monday31+1
		elif row["Zone"] == "32":
			Monday32 = Monday32+1
		elif row["Zone"] == "33":
			Monday33 = Monday33+1
		elif row["Zone"] == "34":
			Monday34 = Monday34+1
		elif row["Zone"] == "35":
			Monday35 = Monday35+1
		elif row["Zone"] == "36":
			Monday36 = Monday36+1
		elif row["Zone"] == "37":
			Monday37 = Monday37+1
		elif row["Zone"] == "38":
			Monday38 = Monday38+1
		elif row["Zone"] == "39":
			Monday39 = Monday39+1
		elif row["Zone"] == "40":
			Monday40 = Monday40+1

		elif row["Zone"] == "41":
			Monday41 = Monday41+1
		elif row["Zone"] == "42":
			Monday42 = Monday42+1
		elif row["Zone"] == "43":
			Monday43 = Monday43+1
		elif row["Zone"] == "44":
			Monday44 = Monday44+1
		elif row["Zone"] == "45":
			Monday45 = Monday45+1
		elif row["Zone"] == "46":
			Monday46 = Monday46+1
		elif row["Zone"] == "47":
			Monday47 = Monday47+1
		elif row["Zone"] == "48":
			Monday48 = Monday48+1
		elif row["Zone"] == "49":
			Monday49 = Monday49+1
		elif row["Zone"] == "50":
			Monday50 = Monday50+1

		elif row["Zone"] == "51":
			Monday51 = Monday51+1
		elif row["Zone"] == "52":
			Monday52 = Monday52+1
		elif row["Zone"] == "53":
			Monday53 = Monday53+1
		elif row["Zone"] == "54":
			Monday54 = Monday54+1
		elif row["Zone"] == "55":
			Monday55 = Monday55+1
		elif row["Zone"] == "56":
			Monday56 = Monday56+1
		elif row["Zone"] == "57":
			Monday57 = Monday57+1
		elif row["Zone"] == "58":
			Monday58 = Monday58+1
		elif row["Zone"] == "59":
			Monday59 = Monday59+1
		elif row["Zone"] == "60":
			Monday60 = Monday60+1

		elif row["Zone"] == "61":
			Monday61 = Monday61+1
		elif row["Zone"] == "62":
			Monday62 = Monday62+1
		elif row["Zone"] == "63":
			Monday63 = Monday63+1
		elif row["Zone"] == "64":
			Monday64 = Monday64+1
		elif row["Zone"] == "65":
			Monday65 = Monday65+1
		elif row["Zone"] == "66":
			Monday66 = Monday66+1
		elif row["Zone"] == "67":
			Monday67 = Monday67+1
		elif row["Zone"] == "68":
			Monday68 = Monday68+1
		elif row["Zone"] == "69":
			Monday69 = Monday69+1
		elif row["Zone"] == "70":
			Monday70 = Monday70+1

		elif row["Zone"] == "71":
			Monday71 = Monday71+1
		elif row["Zone"] == "72":
			Monday72 = Monday72+1
		elif row["Zone"] == "73":
			Monday73 = Monday73+1
		elif row["Zone"] == "74":
			Monday74 = Monday74+1
		elif row["Zone"] == "75":
			Monday75 = Monday75+1
		elif row["Zone"] == "76":
			Monday76 = Monday76+1
		elif row["Zone"] == "77":
			Monday77 = Monday77+1
		elif row["Zone"] == "78":
			Monday78 = Monday78+1
		elif row["Zone"] == "79":
			Monday79 = Monday79+1
		elif row["Zone"] == "80":
			Monday80 = Monday80+1

		elif row["Zone"] == "81":
			Monday81 = Monday81+1
		elif row["Zone"] == "82":
			Monday82 = Monday82+1
		elif row["Zone"] == "83":
			Monday83 = Monday83+1
		elif row["Zone"] == "84":
			Monday84 = Monday84+1
		elif row["Zone"] == "85":
			Monday85 = Monday85+1
		elif row["Zone"] == "86":
			Monday86 = Monday86+1
		elif row["Zone"] == "87":
			Monday87 = Monday87+1
		elif row["Zone"] == "88":
			Monday88 = Monday88+1
		elif row["Zone"] == "89":
			Monday89 = Monday89+1
		elif row["Zone"] == "90":
			Monday90 = Monday90+1

		elif row["Zone"] == "91":
			Monday91 = Monday91+1
		elif row["Zone"] == "92":
			Monday92 = Monday92+1
		elif row["Zone"] == "93":
			Monday93 = Monday93+1
		elif row["Zone"] == "94":
			Monday94 = Monday94+1
		elif row["Zone"] == "95":
			Monday95 = Monday95+1
		elif row["Zone"] == "96":
			Monday96 = Monday96+1
		
	########################### Monday HERE #########################

		
	########################### TUESDAY HERE #########################

	elif "Tuesday" in row["Day"]:
		
		if row["Zone"] == "1":
			Tuesday1 = Tuesday1+1
		elif row["Zone"] == "2":
			Tuesday2 = Tuesday2+1
		elif row["Zone"] == "3":
			Tuesday3 = Tuesday3+1
		elif row["Zone"] == "4":
			Tuesday4 = Tuesday4+1
		elif row["Zone"] == "5":
			Tuesday5 = Tuesday5+1
		elif row["Zone"] == "6":
			Tuesday6 = Tuesday6+1
		elif row["Zone"] == "7":
			Tuesday7 = Tuesday7+1
		elif row["Zone"] == "8":
			Tuesday8 = Tuesday8+1
		elif row["Zone"] == "9":
			Tuesday9 = Tuesday9+1
		elif row["Zone"] == "10":
			Tuesday10 = Tuesday10+1

		elif row["Zone"] == "11":
			Tuesday11 = Tuesday11+1
		elif row["Zone"] == "12":
			Tuesday12 = Tuesday12+1
		elif row["Zone"] == "13":
			Tuesday13 = Tuesday13+1
		elif row["Zone"] == "14":
			Tuesday14 = Tuesday14+1
		elif row["Zone"] == "15":
			Tuesday15 = Tuesday15+1
		elif row["Zone"] == "16":
			Tuesday16 = Tuesday16+1
		elif row["Zone"] == "17":
			Tuesday17 = Tuesday17+1
		elif row["Zone"] == "18":
			Tuesday18 = Tuesday18+1
		elif row["Zone"] == "19":
			Tuesday19 = Tuesday19+1
		elif row["Zone"] == "20":
			Tuesday20 = Tuesday20+1


		elif row["Zone"] == "21":
			Tuesday21 = Tuesday21+1
		elif row["Zone"] == "22":
			Tuesday2 = Tuesday2+1
		elif row["Zone"] == "23":
			Tuesday23 = Tuesday23+1
		elif row["Zone"] == "24":
			Tuesday24 = Tuesday24+1
		elif row["Zone"] == "25":
			Tuesday25 = Tuesday25+1
		elif row["Zone"] == "26":
			Tuesday26 = Tuesday26+1
		elif row["Zone"] == "27":
			Tuesday27 = Tuesday27+1
		elif row["Zone"] == "28":
			Tuesday28 = Tuesday28+1
		elif row["Zone"] == "29":
			Tuesday29 = Tuesday29+1
		elif row["Zone"] == "10":
			Tuesday30 = Tuesday30+1

		elif row["Zone"] == "31":
			Tuesday31 = Tuesday31+1
		elif row["Zone"] == "32":
			Tuesday32 = Tuesday32+1
		elif row["Zone"] == "33":
			Tuesday33 = Tuesday33+1
		elif row["Zone"] == "34":
			Tuesday34 = Tuesday34+1
		elif row["Zone"] == "35":
			Tuesday35 = Tuesday35+1
		elif row["Zone"] == "36":
			Tuesday36 = Tuesday36+1
		elif row["Zone"] == "37":
			Tuesday37 = Tuesday37+1
		elif row["Zone"] == "38":
			Tuesday38 = Tuesday38+1
		elif row["Zone"] == "39":
			Tuesday39 = Tuesday39+1
		elif row["Zone"] == "40":
			Tuesday40 = Tuesday40+1

		elif row["Zone"] == "41":
			Tuesday41 = Tuesday41+1
		elif row["Zone"] == "42":
			Tuesday42 = Tuesday42+1
		elif row["Zone"] == "43":
			Tuesday43 = Tuesday43+1
		elif row["Zone"] == "44":
			Tuesday44 = Tuesday44+1
		elif row["Zone"] == "45":
			Tuesday45 = Tuesday45+1
		elif row["Zone"] == "46":
			Tuesday46 = Tuesday46+1
		elif row["Zone"] == "47":
			Tuesday47 = Tuesday47+1
		elif row["Zone"] == "48":
			Tuesday48 = Tuesday48+1
		elif row["Zone"] == "49":
			Tuesday49 = Tuesday49+1
		elif row["Zone"] == "50":
			Tuesday50 = Tuesday50+1

		elif row["Zone"] == "51":
			Tuesday51 = Tuesday51+1
		elif row["Zone"] == "52":
			Tuesday52 = Tuesday52+1
		elif row["Zone"] == "53":
			Tuesday53 = Tuesday53+1
		elif row["Zone"] == "54":
			Tuesday54 = Tuesday54+1
		elif row["Zone"] == "55":
			Tuesday55 = Tuesday55+1
		elif row["Zone"] == "56":
			Tuesday56 = Tuesday56+1
		elif row["Zone"] == "57":
			Tuesday57 = Tuesday57+1
		elif row["Zone"] == "58":
			Tuesday58 = Tuesday58+1
		elif row["Zone"] == "59":
			Tuesday59 = Tuesday59+1
		elif row["Zone"] == "60":
			Tuesday60 = Tuesday60+1

		elif row["Zone"] == "61":
			Tuesday61 = Tuesday61+1
		elif row["Zone"] == "62":
			Tuesday62 = Tuesday62+1
		elif row["Zone"] == "63":
			Tuesday63 = Tuesday63+1
		elif row["Zone"] == "64":
			Tuesday64 = Tuesday64+1
		elif row["Zone"] == "65":
			Tuesday65 = Tuesday65+1
		elif row["Zone"] == "66":
			Tuesday66 = Tuesday66+1
		elif row["Zone"] == "67":
			Tuesday67 = Tuesday67+1
		elif row["Zone"] == "68":
			Tuesday68 = Tuesday68+1
		elif row["Zone"] == "69":
			Tuesday69 = Tuesday69+1
		elif row["Zone"] == "70":
			Tuesday70 = Tuesday70+1

		elif row["Zone"] == "71":
			Tuesday71 = Tuesday71+1
		elif row["Zone"] == "72":
			Tuesday72 = Tuesday72+1
		elif row["Zone"] == "73":
			Tuesday73 = Tuesday73+1
		elif row["Zone"] == "74":
			Tuesday74 = Tuesday74+1
		elif row["Zone"] == "75":
			Tuesday75 = Tuesday75+1
		elif row["Zone"] == "76":
			Tuesday76 = Tuesday76+1
		elif row["Zone"] == "77":
			Tuesday77 = Tuesday77+1
		elif row["Zone"] == "78":
			Tuesday78 = Tuesday78+1
		elif row["Zone"] == "79":
			Tuesday79 = Tuesday79+1
		elif row["Zone"] == "80":
			Tuesday80 = Tuesday80+1

		elif row["Zone"] == "81":
			Tuesday81 = Tuesday81+1
		elif row["Zone"] == "82":
			Tuesday82 = Tuesday82+1
		elif row["Zone"] == "83":
			Tuesday83 = Tuesday83+1
		elif row["Zone"] == "84":
			Tuesday84 = Tuesday84+1
		elif row["Zone"] == "85":
			Tuesday85 = Tuesday85+1
		elif row["Zone"] == "86":
			Tuesday86 = Tuesday86+1
		elif row["Zone"] == "87":
			Tuesday87 = Tuesday87+1
		elif row["Zone"] == "88":
			Tuesday88 = Tuesday88+1
		elif row["Zone"] == "89":
			Tuesday89 = Tuesday89+1
		elif row["Zone"] == "90":
			Tuesday90 = Tuesday90+1

		elif row["Zone"] == "91":
			Tuesday91 = Tuesday91+1
		elif row["Zone"] == "92":
			Tuesday92 = Tuesday92+1
		elif row["Zone"] == "93":
			Tuesday93 = Tuesday93+1
		elif row["Zone"] == "94":
			Tuesday94 = Tuesday94+1
		elif row["Zone"] == "95":
			Tuesday95 = Tuesday95+1
		elif row["Zone"] == "96":
			Tuesday96 = Tuesday96+1
		
	########################### Tuesday HERE #########################

		
		
	########################### WEDNESDAY HERE #########################

	elif "Wednesday" in row["Day"]:
		
		if row["Zone"] == "1":
			Wednesday1 = Wednesday1+1
		elif row["Zone"] == "2":
			Wednesday2 = Wednesday2+1
		elif row["Zone"] == "3":
			Wednesday3 = Wednesday3+1
		elif row["Zone"] == "4":
			Wednesday4 = Wednesday4+1
		elif row["Zone"] == "5":
			Wednesday5 = Wednesday5+1
		elif row["Zone"] == "6":
			Wednesday6 = Wednesday6+1
		elif row["Zone"] == "7":
			Wednesday7 = Wednesday7+1
		elif row["Zone"] == "8":
			Wednesday8 = Wednesday8+1
		elif row["Zone"] == "9":
			Wednesday9 = Wednesday9+1
		elif row["Zone"] == "10":
			Wednesday10 = Wednesday10+1

		elif row["Zone"] == "11":
			Wednesday11 = Wednesday11+1
		elif row["Zone"] == "12":
			Wednesday12 = Wednesday12+1
		elif row["Zone"] == "13":
			Wednesday13 = Wednesday13+1
		elif row["Zone"] == "14":
			Wednesday14 = Wednesday14+1
		elif row["Zone"] == "15":
			Wednesday15 = Wednesday15+1
		elif row["Zone"] == "16":
			Wednesday16 = Wednesday16+1
		elif row["Zone"] == "17":
			Wednesday17 = Wednesday17+1
		elif row["Zone"] == "18":
			Wednesday18 = Wednesday18+1
		elif row["Zone"] == "19":
			Wednesday19 = Wednesday19+1
		elif row["Zone"] == "20":
			Wednesday20 = Wednesday20+1


		elif row["Zone"] == "21":
			Wednesday21 = Wednesday21+1
		elif row["Zone"] == "22":
			Wednesday2 = Wednesday2+1
		elif row["Zone"] == "23":
			Wednesday23 = Wednesday23+1
		elif row["Zone"] == "24":
			Wednesday24 = Wednesday24+1
		elif row["Zone"] == "25":
			Wednesday25 = Wednesday25+1
		elif row["Zone"] == "26":
			Wednesday26 = Wednesday26+1
		elif row["Zone"] == "27":
			Wednesday27 = Wednesday27+1
		elif row["Zone"] == "28":
			Wednesday28 = Wednesday28+1
		elif row["Zone"] == "29":
			Wednesday29 = Wednesday29+1
		elif row["Zone"] == "10":
			Wednesday30 = Wednesday30+1

		elif row["Zone"] == "31":
			Wednesday31 = Wednesday31+1
		elif row["Zone"] == "32":
			Wednesday32 = Wednesday32+1
		elif row["Zone"] == "33":
			Wednesday33 = Wednesday33+1
		elif row["Zone"] == "34":
			Wednesday34 = Wednesday34+1
		elif row["Zone"] == "35":
			Wednesday35 = Wednesday35+1
		elif row["Zone"] == "36":
			Wednesday36 = Wednesday36+1
		elif row["Zone"] == "37":
			Wednesday37 = Wednesday37+1
		elif row["Zone"] == "38":
			Wednesday38 = Wednesday38+1
		elif row["Zone"] == "39":
			Wednesday39 = Wednesday39+1
		elif row["Zone"] == "40":
			Wednesday40 = Wednesday40+1

		elif row["Zone"] == "41":
			Wednesday41 = Wednesday41+1
		elif row["Zone"] == "42":
			Wednesday42 = Wednesday42+1
		elif row["Zone"] == "43":
			Wednesday43 = Wednesday43+1
		elif row["Zone"] == "44":
			Wednesday44 = Wednesday44+1
		elif row["Zone"] == "45":
			Wednesday45 = Wednesday45+1
		elif row["Zone"] == "46":
			Wednesday46 = Wednesday46+1
		elif row["Zone"] == "47":
			Wednesday47 = Wednesday47+1
		elif row["Zone"] == "48":
			Wednesday48 = Wednesday48+1
		elif row["Zone"] == "49":
			Wednesday49 = Wednesday49+1
		elif row["Zone"] == "50":
			Wednesday50 = Wednesday50+1

		elif row["Zone"] == "51":
			Wednesday51 = Wednesday51+1
		elif row["Zone"] == "52":
			Wednesday52 = Wednesday52+1
		elif row["Zone"] == "53":
			Wednesday53 = Wednesday53+1
		elif row["Zone"] == "54":
			Wednesday54 = Wednesday54+1
		elif row["Zone"] == "55":
			Wednesday55 = Wednesday55+1
		elif row["Zone"] == "56":
			Wednesday56 = Wednesday56+1
		elif row["Zone"] == "57":
			Wednesday57 = Wednesday57+1
		elif row["Zone"] == "58":
			Wednesday58 = Wednesday58+1
		elif row["Zone"] == "59":
			Wednesday59 = Wednesday59+1
		elif row["Zone"] == "60":
			Wednesday60 = Wednesday60+1

		elif row["Zone"] == "61":
			Wednesday61 = Wednesday61+1
		elif row["Zone"] == "62":
			Wednesday62 = Wednesday62+1
		elif row["Zone"] == "63":
			Wednesday63 = Wednesday63+1
		elif row["Zone"] == "64":
			Wednesday64 = Wednesday64+1
		elif row["Zone"] == "65":
			Wednesday65 = Wednesday65+1
		elif row["Zone"] == "66":
			Wednesday66 = Wednesday66+1
		elif row["Zone"] == "67":
			Wednesday67 = Wednesday67+1
		elif row["Zone"] == "68":
			Wednesday68 = Wednesday68+1
		elif row["Zone"] == "69":
			Wednesday69 = Wednesday69+1
		elif row["Zone"] == "70":
			Wednesday70 = Wednesday70+1

		elif row["Zone"] == "71":
			Wednesday71 = Wednesday71+1
		elif row["Zone"] == "72":
			Wednesday72 = Wednesday72+1
		elif row["Zone"] == "73":
			Wednesday73 = Wednesday73+1
		elif row["Zone"] == "74":
			Wednesday74 = Wednesday74+1
		elif row["Zone"] == "75":
			Wednesday75 = Wednesday75+1
		elif row["Zone"] == "76":
			Wednesday76 = Wednesday76+1
		elif row["Zone"] == "77":
			Wednesday77 = Wednesday77+1
		elif row["Zone"] == "78":
			Wednesday78 = Wednesday78+1
		elif row["Zone"] == "79":
			Wednesday79 = Wednesday79+1
		elif row["Zone"] == "80":
			Wednesday80 = Wednesday80+1

		elif row["Zone"] == "81":
			Wednesday81 = Wednesday81+1
		elif row["Zone"] == "82":
			Wednesday82 = Wednesday82+1
		elif row["Zone"] == "83":
			Wednesday83 = Wednesday83+1
		elif row["Zone"] == "84":
			Wednesday84 = Wednesday84+1
		elif row["Zone"] == "85":
			Wednesday85 = Wednesday85+1
		elif row["Zone"] == "86":
			Wednesday86 = Wednesday86+1
		elif row["Zone"] == "87":
			Wednesday87 = Wednesday87+1
		elif row["Zone"] == "88":
			Wednesday88 = Wednesday88+1
		elif row["Zone"] == "89":
			Wednesday89 = Wednesday89+1
		elif row["Zone"] == "90":
			Wednesday90 = Wednesday90+1

		elif row["Zone"] == "91":
			Wednesday91 = Wednesday91+1
		elif row["Zone"] == "92":
			Wednesday92 = Wednesday92+1
		elif row["Zone"] == "93":
			Wednesday93 = Wednesday93+1
		elif row["Zone"] == "94":
			Wednesday94 = Wednesday94+1
		elif row["Zone"] == "95":
			Wednesday95 = Wednesday95+1
		elif row["Zone"] == "96":
			Wednesday96 = Wednesday96+1
		
	########################### Wednesday HERE #########################

		
		
	########################### THURSDAY HERE #########################

	elif "Thursday" in row["Day"]:
		if row["Zone"] == "1":
			Thursday1 = Thursday1+1
		elif row["Zone"] == "2":
			Thursday2 = Thursday2+1
		elif row["Zone"] == "3":
			Thursday3 = Thursday3+1
		elif row["Zone"] == "4":
			Thursday4 = Thursday4+1
		elif row["Zone"] == "5":
			Thursday5 = Thursday5+1
		elif row["Zone"] == "6":
			Thursday6 = Thursday6+1
		elif row["Zone"] == "7":
			Thursday7 = Thursday7+1
		elif row["Zone"] == "8":
			Thursday8 = Thursday8+1
		elif row["Zone"] == "9":
			Thursday9 = Thursday9+1
		elif row["Zone"] == "10":
			Thursday10 = Thursday10+1

		elif row["Zone"] == "11":
			Thursday11 = Thursday11+1
		elif row["Zone"] == "12":
			Thursday12 = Thursday12+1
		elif row["Zone"] == "13":
			Thursday13 = Thursday13+1
		elif row["Zone"] == "14":
			Thursday14 = Thursday14+1
		elif row["Zone"] == "15":
			Thursday15 = Thursday15+1
		elif row["Zone"] == "16":
			Thursday16 = Thursday16+1
		elif row["Zone"] == "17":
			Thursday17 = Thursday17+1
		elif row["Zone"] == "18":
			Thursday18 = Thursday18+1
		elif row["Zone"] == "19":
			Thursday19 = Thursday19+1
		elif row["Zone"] == "20":
			Thursday20 = Thursday20+1


		elif row["Zone"] == "21":
			Thursday21 = Thursday21+1
		elif row["Zone"] == "22":
			Thursday2 = Thursday2+1
		elif row["Zone"] == "23":
			Thursday23 = Thursday23+1
		elif row["Zone"] == "24":
			Thursday24 = Thursday24+1
		elif row["Zone"] == "25":
			Thursday25 = Thursday25+1
		elif row["Zone"] == "26":
			Thursday26 = Thursday26+1
		elif row["Zone"] == "27":
			Thursday27 = Thursday27+1
		elif row["Zone"] == "28":
			Thursday28 = Thursday28+1
		elif row["Zone"] == "29":
			Thursday29 = Thursday29+1
		elif row["Zone"] == "10":
			Thursday30 = Thursday30+1

		elif row["Zone"] == "31":
			Thursday31 = Thursday31+1
		elif row["Zone"] == "32":
			Thursday32 = Thursday32+1
		elif row["Zone"] == "33":
			Thursday33 = Thursday33+1
		elif row["Zone"] == "34":
			Thursday34 = Thursday34+1
		elif row["Zone"] == "35":
			Thursday35 = Thursday35+1
		elif row["Zone"] == "36":
			Thursday36 = Thursday36+1
		elif row["Zone"] == "37":
			Thursday37 = Thursday37+1
		elif row["Zone"] == "38":
			Thursday38 = Thursday38+1
		elif row["Zone"] == "39":
			Thursday39 = Thursday39+1
		elif row["Zone"] == "40":
			Thursday40 = Thursday40+1

		elif row["Zone"] == "41":
			Thursday41 = Thursday41+1
		elif row["Zone"] == "42":
			Thursday42 = Thursday42+1
		elif row["Zone"] == "43":
			Thursday43 = Thursday43+1
		elif row["Zone"] == "44":
			Thursday44 = Thursday44+1
		elif row["Zone"] == "45":
			Thursday45 = Thursday45+1
		elif row["Zone"] == "46":
			Thursday46 = Thursday46+1
		elif row["Zone"] == "47":
			Thursday47 = Thursday47+1
		elif row["Zone"] == "48":
			Thursday48 = Thursday48+1
		elif row["Zone"] == "49":
			Thursday49 = Thursday49+1
		elif row["Zone"] == "50":
			Thursday50 = Thursday50+1

		elif row["Zone"] == "51":
			Thursday51 = Thursday51+1
		elif row["Zone"] == "52":
			Thursday52 = Thursday52+1
		elif row["Zone"] == "53":
			Thursday53 = Thursday53+1
		elif row["Zone"] == "54":
			Thursday54 = Thursday54+1
		elif row["Zone"] == "55":
			Thursday55 = Thursday55+1
		elif row["Zone"] == "56":
			Thursday56 = Thursday56+1
		elif row["Zone"] == "57":
			Thursday57 = Thursday57+1
		elif row["Zone"] == "58":
			Thursday58 = Thursday58+1
		elif row["Zone"] == "59":
			Thursday59 = Thursday59+1
		elif row["Zone"] == "60":
			Thursday60 = Thursday60+1

		elif row["Zone"] == "61":
			Thursday61 = Thursday61+1
		elif row["Zone"] == "62":
			Thursday62 = Thursday62+1
		elif row["Zone"] == "63":
			Thursday63 = Thursday63+1
		elif row["Zone"] == "64":
			Thursday64 = Thursday64+1
		elif row["Zone"] == "65":
			Thursday65 = Thursday65+1
		elif row["Zone"] == "66":
			Thursday66 = Thursday66+1
		elif row["Zone"] == "67":
			Thursday67 = Thursday67+1
		elif row["Zone"] == "68":
			Thursday68 = Thursday68+1
		elif row["Zone"] == "69":
			Thursday69 = Thursday69+1
		elif row["Zone"] == "70":
			Thursday70 = Thursday70+1

		elif row["Zone"] == "71":
			Thursday71 = Thursday71+1
		elif row["Zone"] == "72":
			Thursday72 = Thursday72+1
		elif row["Zone"] == "73":
			Thursday73 = Thursday73+1
		elif row["Zone"] == "74":
			Thursday74 = Thursday74+1
		elif row["Zone"] == "75":
			Thursday75 = Thursday75+1
		elif row["Zone"] == "76":
			Thursday76 = Thursday76+1
		elif row["Zone"] == "77":
			Thursday77 = Thursday77+1
		elif row["Zone"] == "78":
			Thursday78 = Thursday78+1
		elif row["Zone"] == "79":
			Thursday79 = Thursday79+1
		elif row["Zone"] == "80":
			Thursday80 = Thursday80+1

		elif row["Zone"] == "81":
			Thursday81 = Thursday81+1
		elif row["Zone"] == "82":
			Thursday82 = Thursday82+1
		elif row["Zone"] == "83":
			Thursday83 = Thursday83+1
		elif row["Zone"] == "84":
			Thursday84 = Thursday84+1
		elif row["Zone"] == "85":
			Thursday85 = Thursday85+1
		elif row["Zone"] == "86":
			Thursday86 = Thursday86+1
		elif row["Zone"] == "87":
			Thursday87 = Thursday87+1
		elif row["Zone"] == "88":
			Thursday88 = Thursday88+1
		elif row["Zone"] == "89":
			Thursday89 = Thursday89+1
		elif row["Zone"] == "90":
			Thursday90 = Thursday90+1

		elif row["Zone"] == "91":
			Thursday91 = Thursday91+1
		elif row["Zone"] == "92":
			Thursday92 = Thursday92+1
		elif row["Zone"] == "93":
			Thursday93 = Thursday93+1
		elif row["Zone"] == "94":
			Thursday94 = Thursday94+1
		elif row["Zone"] == "95":
			Thursday95 = Thursday95+1
		elif row["Zone"] == "96":
			Thursday96 = Thursday96+1
		
	########################### Thursday HERE #########################




		
	########################### Friday HERE #########################

	elif "Friday" in row["Day"]:
		if row["Zone"] == "1":
			Friday1 = Friday1+1
		elif row["Zone"] == "2":
			Friday2 = Friday2+1
		elif row["Zone"] == "3":
			Friday3 = Friday3+1
		elif row["Zone"] == "4":
			Friday4 = Friday4+1
		elif row["Zone"] == "5":
			Friday5 = Friday5+1
		elif row["Zone"] == "6":
			Friday6 = Friday6+1
		elif row["Zone"] == "7":
			Friday7 = Friday7+1
		elif row["Zone"] == "8":
			Friday8 = Friday8+1
		elif row["Zone"] == "9":
			Friday9 = Friday9+1
		elif row["Zone"] == "10":
			Friday10 = Friday10+1

		elif row["Zone"] == "11":
			Friday11 = Friday11+1
		elif row["Zone"] == "12":
			Friday12 = Friday12+1
		elif row["Zone"] == "13":
			Friday13 = Friday13+1
		elif row["Zone"] == "14":
			Friday14 = Friday14+1
		elif row["Zone"] == "15":
			Friday15 = Friday15+1
		elif row["Zone"] == "16":
			Friday16 = Friday16+1
		elif row["Zone"] == "17":
			Friday17 = Friday17+1
		elif row["Zone"] == "18":
			Friday18 = Friday18+1
		elif row["Zone"] == "19":
			Friday19 = Friday19+1
		elif row["Zone"] == "20":
			Friday20 = Friday20+1


		elif row["Zone"] == "21":
			Friday21 = Friday21+1
		elif row["Zone"] == "22":
			Friday2 = Friday2+1
		elif row["Zone"] == "23":
			Friday23 = Friday23+1
		elif row["Zone"] == "24":
			Friday24 = Friday24+1
		elif row["Zone"] == "25":
			Friday25 = Friday25+1
		elif row["Zone"] == "26":
			Friday26 = Friday26+1
		elif row["Zone"] == "27":
			Friday27 = Friday27+1
		elif row["Zone"] == "28":
			Friday28 = Friday28+1
		elif row["Zone"] == "29":
			Friday29 = Friday29+1
		elif row["Zone"] == "10":
			Friday30 = Friday30+1

		elif row["Zone"] == "31":
			Friday31 = Friday31+1
		elif row["Zone"] == "32":
			Friday32 = Friday32+1
		elif row["Zone"] == "33":
			Friday33 = Friday33+1
		elif row["Zone"] == "34":
			Friday34 = Friday34+1
		elif row["Zone"] == "35":
			Friday35 = Friday35+1
		elif row["Zone"] == "36":
			Friday36 = Friday36+1
		elif row["Zone"] == "37":
			Friday37 = Friday37+1
		elif row["Zone"] == "38":
			Friday38 = Friday38+1
		elif row["Zone"] == "39":
			Friday39 = Friday39+1
		elif row["Zone"] == "40":
			Friday40 = Friday40+1

		elif row["Zone"] == "41":
			Friday41 = Friday41+1
		elif row["Zone"] == "42":
			Friday42 = Friday42+1
		elif row["Zone"] == "43":
			Friday43 = Friday43+1
		elif row["Zone"] == "44":
			Friday44 = Friday44+1
		elif row["Zone"] == "45":
			Friday45 = Friday45+1
		elif row["Zone"] == "46":
			Friday46 = Friday46+1
		elif row["Zone"] == "47":
			Friday47 = Friday47+1
		elif row["Zone"] == "48":
			Friday48 = Friday48+1
		elif row["Zone"] == "49":
			Friday49 = Friday49+1
		elif row["Zone"] == "50":
			Friday50 = Friday50+1

		elif row["Zone"] == "51":
			Friday51 = Friday51+1
		elif row["Zone"] == "52":
			Friday52 = Friday52+1
		elif row["Zone"] == "53":
			Friday53 = Friday53+1
		elif row["Zone"] == "54":
			Friday54 = Friday54+1
		elif row["Zone"] == "55":
			Friday55 = Friday55+1
		elif row["Zone"] == "56":
			Friday56 = Friday56+1
		elif row["Zone"] == "57":
			Friday57 = Friday57+1
		elif row["Zone"] == "58":
			Friday58 = Friday58+1
		elif row["Zone"] == "59":
			Friday59 = Friday59+1
		elif row["Zone"] == "60":
			Friday60 = Friday60+1

		elif row["Zone"] == "61":
			Friday61 = Friday61+1
		elif row["Zone"] == "62":
			Friday62 = Friday62+1
		elif row["Zone"] == "63":
			Friday63 = Friday63+1
		elif row["Zone"] == "64":
			Friday64 = Friday64+1
		elif row["Zone"] == "65":
			Friday65 = Friday65+1
		elif row["Zone"] == "66":
			Friday66 = Friday66+1
		elif row["Zone"] == "67":
			Friday67 = Friday67+1
		elif row["Zone"] == "68":
			Friday68 = Friday68+1
		elif row["Zone"] == "69":
			Friday69 = Friday69+1
		elif row["Zone"] == "70":
			Friday70 = Friday70+1

		elif row["Zone"] == "71":
			Friday71 = Friday71+1
		elif row["Zone"] == "72":
			Friday72 = Friday72+1
		elif row["Zone"] == "73":
			Friday73 = Friday73+1
		elif row["Zone"] == "74":
			Friday74 = Friday74+1
		elif row["Zone"] == "75":
			Friday75 = Friday75+1
		elif row["Zone"] == "76":
			Friday76 = Friday76+1
		elif row["Zone"] == "77":
			Friday77 = Friday77+1
		elif row["Zone"] == "78":
			Friday78 = Friday78+1
		elif row["Zone"] == "79":
			Friday79 = Friday79+1
		elif row["Zone"] == "80":
			Friday80 = Friday80+1

		elif row["Zone"] == "81":
			Friday81 = Friday81+1
		elif row["Zone"] == "82":
			Friday82 = Friday82+1
		elif row["Zone"] == "83":
			Friday83 = Friday83+1
		elif row["Zone"] == "84":
			Friday84 = Friday84+1
		elif row["Zone"] == "85":
			Friday85 = Friday85+1
		elif row["Zone"] == "86":
			Friday86 = Friday86+1
		elif row["Zone"] == "87":
			Friday87 = Friday87+1
		elif row["Zone"] == "88":
			Friday88 = Friday88+1
		elif row["Zone"] == "89":
			Friday89 = Friday89+1
		elif row["Zone"] == "90":
			Friday90 = Friday90+1

		elif row["Zone"] == "91":
			Friday91 = Friday91+1
		elif row["Zone"] == "92":
			Friday92 = Friday92+1
		elif row["Zone"] == "93":
			Friday93 = Friday93+1
		elif row["Zone"] == "94":
			Friday94 = Friday94+1
		elif row["Zone"] == "95":
			Friday95 = Friday95+1
		elif row["Zone"] == "96":
			Friday96 = Friday96+1

		
	########################### Saturday HERE #########################

	elif "Saturday" in row["Day"]:
		if row["Zone"] == "1":
			Saturday1 = Saturday1+1
		elif row["Zone"] == "2":
			Saturday2 = Saturday2+1
		elif row["Zone"] == "3":
			Saturday3 = Saturday3+1
		elif row["Zone"] == "4":
			Saturday4 = Saturday4+1
		elif row["Zone"] == "5":
			Saturday5 = Saturday5+1
		elif row["Zone"] == "6":
			Saturday6 = Saturday6+1
		elif row["Zone"] == "7":
			Saturday7 = Saturday7+1
		elif row["Zone"] == "8":
			Saturday8 = Saturday8+1
		elif row["Zone"] == "9":
			Saturday9 = Saturday9+1
		elif row["Zone"] == "10":
			Saturday10 = Saturday10+1

		elif row["Zone"] == "11":
			Saturday11 = Saturday11+1
		elif row["Zone"] == "12":
			Saturday12 = Saturday12+1
		elif row["Zone"] == "13":
			Saturday13 = Saturday13+1
		elif row["Zone"] == "14":
			Saturday14 = Saturday14+1
		elif row["Zone"] == "15":
			Saturday15 = Saturday15+1
		elif row["Zone"] == "16":
			Saturday16 = Saturday16+1
		elif row["Zone"] == "17":
			Saturday17 = Saturday17+1
		elif row["Zone"] == "18":
			Saturday18 = Saturday18+1
		elif row["Zone"] == "19":
			Saturday19 = Saturday19+1
		elif row["Zone"] == "20":
			Saturday20 = Saturday20+1


		elif row["Zone"] == "21":
			Saturday21 = Saturday21+1
		elif row["Zone"] == "22":
			Saturday2 = Saturday2+1
		elif row["Zone"] == "23":
			Saturday23 = Saturday23+1
		elif row["Zone"] == "24":
			Saturday24 = Saturday24+1
		elif row["Zone"] == "25":
			Saturday25 = Saturday25+1
		elif row["Zone"] == "26":
			Saturday26 = Saturday26+1
		elif row["Zone"] == "27":
			Saturday27 = Saturday27+1
		elif row["Zone"] == "28":
			Saturday28 = Saturday28+1
		elif row["Zone"] == "29":
			Saturday29 = Saturday29+1
		elif row["Zone"] == "10":
			Saturday30 = Saturday30+1

		elif row["Zone"] == "31":
			Saturday31 = Saturday31+1
		elif row["Zone"] == "32":
			Saturday32 = Saturday32+1
		elif row["Zone"] == "33":
			Saturday33 = Saturday33+1
		elif row["Zone"] == "34":
			Saturday34 = Saturday34+1
		elif row["Zone"] == "35":
			Saturday35 = Saturday35+1
		elif row["Zone"] == "36":
			Saturday36 = Saturday36+1
		elif row["Zone"] == "37":
			Saturday37 = Saturday37+1
		elif row["Zone"] == "38":
			Saturday38 = Saturday38+1
		elif row["Zone"] == "39":
			Saturday39 = Saturday39+1
		elif row["Zone"] == "40":
			Saturday40 = Saturday40+1

		elif row["Zone"] == "41":
			Saturday41 = Saturday41+1
		elif row["Zone"] == "42":
			Saturday42 = Saturday42+1
		elif row["Zone"] == "43":
			Saturday43 = Saturday43+1
		elif row["Zone"] == "44":
			Saturday44 = Saturday44+1
		elif row["Zone"] == "45":
			Saturday45 = Saturday45+1
		elif row["Zone"] == "46":
			Saturday46 = Saturday46+1
		elif row["Zone"] == "47":
			Saturday47 = Saturday47+1
		elif row["Zone"] == "48":
			Saturday48 = Saturday48+1
		elif row["Zone"] == "49":
			Saturday49 = Saturday49+1
		elif row["Zone"] == "50":
			Saturday50 = Saturday50+1

		elif row["Zone"] == "51":
			Saturday51 = Saturday51+1
		elif row["Zone"] == "52":
			Saturday52 = Saturday52+1
		elif row["Zone"] == "53":
			Saturday53 = Saturday53+1
		elif row["Zone"] == "54":
			Saturday54 = Saturday54+1
		elif row["Zone"] == "55":
			Saturday55 = Saturday55+1
		elif row["Zone"] == "56":
			Saturday56 = Saturday56+1
		elif row["Zone"] == "57":
			Saturday57 = Saturday57+1
		elif row["Zone"] == "58":
			Saturday58 = Saturday58+1
		elif row["Zone"] == "59":
			Saturday59 = Saturday59+1
		elif row["Zone"] == "60":
			Saturday60 = Saturday60+1

		elif row["Zone"] == "61":
			Saturday61 = Saturday61+1
		elif row["Zone"] == "62":
			Saturday62 = Saturday62+1
		elif row["Zone"] == "63":
			Saturday63 = Saturday63+1
		elif row["Zone"] == "64":
			Saturday64 = Saturday64+1
		elif row["Zone"] == "65":
			Saturday65 = Saturday65+1
		elif row["Zone"] == "66":
			Saturday66 = Saturday66+1
		elif row["Zone"] == "67":
			Saturday67 = Saturday67+1
		elif row["Zone"] == "68":
			Saturday68 = Saturday68+1
		elif row["Zone"] == "69":
			Saturday69 = Saturday69+1
		elif row["Zone"] == "70":
			Saturday70 = Saturday70+1

		elif row["Zone"] == "71":
			Saturday71 = Saturday71+1
		elif row["Zone"] == "72":
			Saturday72 = Saturday72+1
		elif row["Zone"] == "73":
			Saturday73 = Saturday73+1
		elif row["Zone"] == "74":
			Saturday74 = Saturday74+1
		elif row["Zone"] == "75":
			Saturday75 = Saturday75+1
		elif row["Zone"] == "76":
			Saturday76 = Saturday76+1
		elif row["Zone"] == "77":
			Saturday77 = Saturday77+1
		elif row["Zone"] == "78":
			Saturday78 = Saturday78+1
		elif row["Zone"] == "79":
			Saturday79 = Saturday79+1
		elif row["Zone"] == "80":
			Saturday80 = Saturday80+1

		elif row["Zone"] == "81":
			Saturday81 = Saturday81+1
		elif row["Zone"] == "82":
			Saturday82 = Saturday82+1
		elif row["Zone"] == "83":
			Saturday83 = Saturday83+1
		elif row["Zone"] == "84":
			Saturday84 = Saturday84+1
		elif row["Zone"] == "85":
			Saturday85 = Saturday85+1
		elif row["Zone"] == "86":
			Saturday86 = Saturday86+1
		elif row["Zone"] == "87":
			Saturday87 = Saturday87+1
		elif row["Zone"] == "88":
			Saturday88 = Saturday88+1
		elif row["Zone"] == "89":
			Saturday89 = Saturday89+1
		elif row["Zone"] == "90":
			Saturday90 = Saturday90+1

		elif row["Zone"] == "91":
			Saturday91 = Saturday91+1
		elif row["Zone"] == "92":
			Saturday92 = Saturday92+1
		elif row["Zone"] == "93":
			Saturday93 = Saturday93+1
		elif row["Zone"] == "94":
			Saturday94 = Saturday94+1
		elif row["Zone"] == "95":
			Saturday95 = Saturday95+1
		elif row["Zone"] == "96":
			Saturday96 = Saturday96+1
		
		
	########################### Sunday HERE #########################

	elif "Sunday" in row["Day"]:
		if row["Zone"] == "1":
			Sunday1 = Sunday1+1
		elif row["Zone"] == "2":
			Sunday2 = Sunday2+1
		elif row["Zone"] == "3":
			Sunday3 = Sunday3+1
		elif row["Zone"] == "4":
			Sunday4 = Sunday4+1
		elif row["Zone"] == "5":
			Sunday5 = Sunday5+1
		elif row["Zone"] == "6":
			Sunday6 = Sunday6+1
		elif row["Zone"] == "7":
			Sunday7 = Sunday7+1
		elif row["Zone"] == "8":
			Sunday8 = Sunday8+1
		elif row["Zone"] == "9":
			Sunday9 = Sunday9+1
		elif row["Zone"] == "10":
			Sunday10 = Sunday10+1

		elif row["Zone"] == "11":
			Sunday11 = Sunday11+1
		elif row["Zone"] == "12":
			Sunday12 = Sunday12+1
		elif row["Zone"] == "13":
			Sunday13 = Sunday13+1
		elif row["Zone"] == "14":
			Sunday14 = Sunday14+1
		elif row["Zone"] == "15":
			Sunday15 = Sunday15+1
		elif row["Zone"] == "16":
			Sunday16 = Sunday16+1
		elif row["Zone"] == "17":
			Sunday17 = Sunday17+1
		elif row["Zone"] == "18":
			Sunday18 = Sunday18+1
		elif row["Zone"] == "19":
			Sunday19 = Sunday19+1
		elif row["Zone"] == "20":
			Sunday20 = Sunday20+1


		elif row["Zone"] == "21":
			Sunday21 = Sunday21+1
		elif row["Zone"] == "22":
			Sunday2 = Sunday2+1
		elif row["Zone"] == "23":
			Sunday23 = Sunday23+1
		elif row["Zone"] == "24":
			Sunday24 = Sunday24+1
		elif row["Zone"] == "25":
			Sunday25 = Sunday25+1
		elif row["Zone"] == "26":
			Sunday26 = Sunday26+1
		elif row["Zone"] == "27":
			Sunday27 = Sunday27+1
		elif row["Zone"] == "28":
			Sunday28 = Sunday28+1
		elif row["Zone"] == "29":
			Sunday29 = Sunday29+1
		elif row["Zone"] == "10":
			Sunday30 = Sunday30+1

		elif row["Zone"] == "31":
			Sunday31 = Sunday31+1
		elif row["Zone"] == "32":
			Sunday32 = Sunday32+1
		elif row["Zone"] == "33":
			Sunday33 = Sunday33+1
		elif row["Zone"] == "34":
			Sunday34 = Sunday34+1
		elif row["Zone"] == "35":
			Sunday35 = Sunday35+1
		elif row["Zone"] == "36":
			Sunday36 = Sunday36+1
		elif row["Zone"] == "37":
			Sunday37 = Sunday37+1
		elif row["Zone"] == "38":
			Sunday38 = Sunday38+1
		elif row["Zone"] == "39":
			Sunday39 = Sunday39+1
		elif row["Zone"] == "40":
			Sunday40 = Sunday40+1

		elif row["Zone"] == "41":
			Sunday41 = Sunday41+1
		elif row["Zone"] == "42":
			Sunday42 = Sunday42+1
		elif row["Zone"] == "43":
			Sunday43 = Sunday43+1
		elif row["Zone"] == "44":
			Sunday44 = Sunday44+1
		elif row["Zone"] == "45":
			Sunday45 = Sunday45+1
		elif row["Zone"] == "46":
			Sunday46 = Sunday46+1
		elif row["Zone"] == "47":
			Sunday47 = Sunday47+1
		elif row["Zone"] == "48":
			Sunday48 = Sunday48+1
		elif row["Zone"] == "49":
			Sunday49 = Sunday49+1
		elif row["Zone"] == "50":
			Sunday50 = Sunday50+1

		elif row["Zone"] == "51":
			Sunday51 = Sunday51+1
		elif row["Zone"] == "52":
			Sunday52 = Sunday52+1
		elif row["Zone"] == "53":
			Sunday53 = Sunday53+1
		elif row["Zone"] == "54":
			Sunday54 = Sunday54+1
		elif row["Zone"] == "55":
			Sunday55 = Sunday55+1
		elif row["Zone"] == "56":
			Sunday56 = Sunday56+1
		elif row["Zone"] == "57":
			Sunday57 = Sunday57+1
		elif row["Zone"] == "58":
			Sunday58 = Sunday58+1
		elif row["Zone"] == "59":
			Sunday59 = Sunday59+1
		elif row["Zone"] == "60":
			Sunday60 = Sunday60+1

		elif row["Zone"] == "61":
			Sunday61 = Sunday61+1
		elif row["Zone"] == "62":
			Sunday62 = Sunday62+1
		elif row["Zone"] == "63":
			Sunday63 = Sunday63+1
		elif row["Zone"] == "64":
			Sunday64 = Sunday64+1
		elif row["Zone"] == "65":
			Sunday65 = Sunday65+1
		elif row["Zone"] == "66":
			Sunday66 = Sunday66+1
		elif row["Zone"] == "67":
			Sunday67 = Sunday67+1
		elif row["Zone"] == "68":
			Sunday68 = Sunday68+1
		elif row["Zone"] == "69":
			Sunday69 = Sunday69+1
		elif row["Zone"] == "70":
			Sunday70 = Sunday70+1

		elif row["Zone"] == "71":
			Sunday71 = Sunday71+1
		elif row["Zone"] == "72":
			Sunday72 = Sunday72+1
		elif row["Zone"] == "73":
			Sunday73 = Sunday73+1
		elif row["Zone"] == "74":
			Sunday74 = Sunday74+1
		elif row["Zone"] == "75":
			Sunday75 = Sunday75+1
		elif row["Zone"] == "76":
			Sunday76 = Sunday76+1
		elif row["Zone"] == "77":
			Sunday77 = Sunday77+1
		elif row["Zone"] == "78":
			Sunday78 = Sunday78+1
		elif row["Zone"] == "79":
			Sunday79 = Sunday79+1
		elif row["Zone"] == "80":
			Sunday80 = Sunday80+1

		elif row["Zone"] == "81":
			Sunday81 = Sunday81+1
		elif row["Zone"] == "82":
			Sunday82 = Sunday82+1
		elif row["Zone"] == "83":
			Sunday83 = Sunday83+1
		elif row["Zone"] == "84":
			Sunday84 = Sunday84+1
		elif row["Zone"] == "85":
			Sunday85 = Sunday85+1
		elif row["Zone"] == "86":
			Sunday86 = Sunday86+1
		elif row["Zone"] == "87":
			Sunday87 = Sunday87+1
		elif row["Zone"] == "88":
			Sunday88 = Sunday88+1
		elif row["Zone"] == "89":
			Sunday89 = Sunday89+1
		elif row["Zone"] == "90":
			Sunday90 = Sunday90+1

		elif row["Zone"] == "91":
			Sunday91 = Sunday91+1
		elif row["Zone"] == "92":
			Sunday92 = Sunday92+1
		elif row["Zone"] == "93":
			Sunday93 = Sunday93+1
		elif row["Zone"] == "94":
			Sunday94 = Sunday94+1
		elif row["Zone"] == "95":
			Sunday95 = Sunday95+1
		elif row["Zone"] == "96":
			Sunday96 = Sunday96+1
		
		
	########################### DAY ITERATION FINISH #########################
	
for x in range(0, 97):
	var0 = globals()['Monday%s' % x]
	print (x, var0)

for x in range(0, 97):
	var0 = globals()['Tuesday%s' % x]
	un = x + 100
	print (un, var0)

for x in range(0, 97):
	var0 = globals()['Wednesday%s' % x]
	un = x + 200
	print (un, var0)

for x in range(0, 97):
	var0 = globals()['Thursday%s' % x]
	un = x + 300
	print (un, var0)

for x in range(0, 97):
	var0 = globals()['Friday%s' % x]
	un = x + 400
	print (un, var0)

for x in range(0, 97):
	var0 = globals()['Saturday%s' % x]
	un = x + 500
	print (un, var0)

for x in range(0, 97):
	var0 = globals()['Sunday%s' % x]
	un = x + 600
	print (un, var0)


print "==========FINSIH=============="

