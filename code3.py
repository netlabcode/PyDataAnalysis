
import csv
import datetime

FreqData = open('listFreqSSID.csv')
ReadFreqCSV = csv.DictReader(FreqData, delimiter=',')

newRecord = []


ssIdentifier=1

for row in ReadFreqCSV:
	if "wifi" in row["SSID"]:
		RecordWholeSSID = (row["SSID"])
		wifi, ScanOrConnected, SSID, useless = RecordWholeSSID.split("|", 4)

		
		#Try LOOPING SSID HERE =======================================================================
		originalData = open('wifiALL.csv')
		ReadOriginalCSV = csv.DictReader(originalData, delimiter=';')

		for row in ReadOriginalCSV:
			if SSID in row["Action"]:

				if row["Date"] != "(invalid date)":
					RecordB = (row["Date"])
					YMD, TA  = RecordB.split("T", 2)
					Y, M, D = YMD.split("-", 3)

					HMS, TB =  TA.split(".", 2)
					H, Min, S = HMS.split(":", 3)

					GNU, none = RecordB.split(".", 1)


					intMin = int(Min)
					intH = int(H)

					
					#Locate Zone of time classification
					if intH == 0:
						if intMin in range(0,16):
							Zoner = 1
						elif intMin in range(16,31):
							Zoner = 2
						elif intMin in range(31,46):
							Zoner = 3
						elif intMin in range(46,60):
							Zoner = 4 

					elif intH == 1:
						if intMin in range(0,16):
							Zoner = 5
						elif intMin in range(16,31):
							Zoner = 6
						elif intMin in range(31,46):
							Zoner = 7
						elif intMin in range(46,60):
							Zoner = 8

					elif intH == 2:
						if intMin in range(0,16):
							Zoner = 9
						elif intMin in range(16,31):
							Zoner = 10
						elif intMin in range(31,46):
							Zoner = 11
						elif intMin in range(46,60):
							Zoner = 12

					elif intH == 3:
						if intMin in range(0,16):
							Zoner = 13
						elif intMin in range(16,31):
							Zoner = 14
						elif intMin in range(31,46):
							Zoner = 15
						elif intMin in range(46,60):
							Zoner = 16

					elif intH == 4:
						if intMin in range(0,16):
							Zoner = 17
						elif intMin in range(16,31):
							Zoner = 18
						elif intMin in range(31,46):
							Zoner = 19
						elif intMin in range(46,60):
							Zoner = 20

					elif intH == 5:
						if intMin in range(0,16):
							Zoner = 21
						elif intMin in range(16,31):
							Zoner = 22
						elif intMin in range(31,46):
							Zoner = 23
						elif intMin in range(46,60):
							Zoner = 24

					elif intH == 6:
						if intMin in range(0,16):
							Zoner = 25
						elif intMin in range(16,31):
							Zoner = 26
						elif intMin in range(31,46):
							Zoner = 27
						elif intMin in range(46,60):
							Zoner = 28

					elif intH == 7:
						if intMin in range(0,16):
							Zoner = 29
						elif intMin in range(16,31):
							Zoner = 30
						elif intMin in range(31,46):
							Zoner = 31
						elif intMin in range(46,60):
							Zoner = 32

					elif intH == 8:
						if intMin in range(0,16):
							Zoner = 33
						elif intMin in range(16,31):
							Zoner = 34
						elif intMin in range(31,46):
							Zoner = 35
						elif intMin in range(46,60):
							Zoner = 36

					elif intH == 9:
						if intMin in range(0,16):
							Zoner = 37
						elif intMin in range(16,31):
							Zoner = 38
						elif intMin in range(31,46):
							Zoner = 39
						elif intMin in range(46,60):
							Zoner = 40

					elif intH == 10:
						if intMin in range(0,16):
							Zoner = 41
						elif intMin in range(16,31):
							Zoner = 42
						elif intMin in range(31,46):
							Zoner = 43
						elif intMin in range(46,60):
							Zoner = 44

					elif intH == 11:
						if intMin in range(0,16):
							Zoner = 45
						elif intMin in range(16,31):
							Zoner = 46
						elif intMin in range(31,46):
							Zoner = 47
						elif intMin in range(46,60):
							Zoner = 48

					elif intH == 12:
						if intMin in range(0,16):
							Zoner = 49
						elif intMin in range(16,31):
							Zoner = 50
						elif intMin in range(31,46):
							Zoner = 51
						elif intMin in range(46,60):
							Zoner = 52

					elif intH == 13:
						if intMin in range(0,16):
							Zoner = 53
						elif intMin in range(16,31):
							Zoner = 54
						elif intMin in range(31,46):
							Zoner = 55
						elif intMin in range(46,60):
							Zoner = 56

					elif intH == 14:
						if intMin in range(0,16):
							Zoner = 57
						elif intMin in range(16,31):
							Zoner = 58
						elif intMin in range(31,46):
							Zoner = 59
						elif intMin in range(46,60):
							Zoner = 60

					elif intH == 15:
						if intMin in range(0,16):
							Zoner = 61
						elif intMin in range(16,31):
							Zoner = 62
						elif intMin in range(31,46):
							Zoner = 63
						elif intMin in range(46,60):
							Zoner = 64

					elif intH == 16:
						if intMin in range(0,16):
							Zoner = 65
						elif intMin in range(16,31):
							Zoner = 66
						elif intMin in range(31,46):
							Zoner = 67
						elif intMin in range(46,60):
							Zoner = 68

					elif intH == 17:
						if intMin in range(0,16):
							Zoner = 69
						elif intMin in range(16,31):
							Zoner = 70
						elif intMin in range(31,46):
							Zoner = 71
						elif intMin in range(46,60):
							Zoner = 72

					elif intH == 18:
						if intMin in range(0,16):
							Zoner = 73
						elif intMin in range(16,31):
							Zoner = 74
						elif intMin in range(31,46):
							Zoner = 75
						elif intMin in range(46,60):
							Zoner = 76

					elif intH == 19:
						if intMin in range(0,16):
							Zoner = 77
						elif intMin in range(16,31):
							Zoner = 78
						elif intMin in range(31,46):
							Zoner = 79
						elif intMin in range(46,60):
							Zoner = 80

					elif intH == 20:
						if intMin in range(0,16):
							Zoner = 81
						elif intMin in range(16,31):
							Zoner = 82
						elif intMin in range(31,46):
							Zoner = 83
						elif intMin in range(46,60):
							Zoner = 84

					elif intH == 21:
						if intMin in range(0,16):
							Zoner = 85
						elif intMin in range(16,31):
							Zoner = 86
						elif intMin in range(31,46):
							Zoner = 87
						elif intMin in range(46,60):
							Zoner = 88

					elif intH == 22:
						if intMin in range(0,16):
							Zoner = 89
						elif intMin in range(16,31):
							Zoner = 90
						elif intMin in range(31,46):
							Zoner = 91
						elif intMin in range(46,60):
							Zoner = 92

					elif intH == 23:
						if intMin in range(0,16):
							Zoner = 93
						elif intMin in range(16,31):
							Zoner = 94
						elif intMin in range(31,46):
							Zoner = 95
						elif intMin in range(46,60):
							Zoner = 96

					
					# Get WeekDay Name
					year, month, day = (int(x) for x in YMD.split('-'))    
					ans = datetime.date(year, month, day)
					WeekDay = ans.strftime("%A")

					#Record as newRecord +ssIdentifier+Day+YMD+HMS+Zoner
					Data = [ssIdentifier, WeekDay, GNU, Zoner] 
					newRecord.append(Data)
					
					print "++++++++++++++++"
					print ssIdentifier
					print GNU
					print Zoner
					print WeekDay

		ssIdentifier = ssIdentifier + 1


#Save newRecord as CSV file
FreqData.close()
originalData.close()


file_new = open('Output.csv', 'wb')
writer = csv.writer(file_new, delimiter=',')
writer.writerows(newRecord)

print "================="
print len(newRecord)

file_new.close()

print "======FINISHED==="

#X = row[1]

#print X