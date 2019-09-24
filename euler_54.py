import csv

handOneList = []
handTwoList = []

def fileImporter():
	csvFile = open("G:\\OneDrive\\code\\project_euler\\euler_054\\p054_poker.txt", "r")
	csvReader = csv.reader(csvFile, delimiter=" ")


	row = 0
	col = 0
	for row in csvReader:
		handOne = []
		handTwo = []
		counter = 0
		for col in row:
			if counter < 5:
				handOne.append(makeList(col))
				#print ("handOne: ", handOne)
			else:
				handTwo.append(makeList(col))
				#print ("handTwo: ", handTwo)
			counter += 1
		handOneList.append(handOne)
		handTwoList.append(handTwo)
	csvFile.close()

	#for row in handOneList:
		#print (row)
	print("#####################################")
	#for row in handTwoList:
		#print (row)

def makeList(str):
	list = []
	list.append(str[0])
	list.append(str[1])
	return list

def isFlish(hand):
	suit = ''
	count = 0
	proceed = True
	for col in hand:
		#print("testpoint_1")
		if  count == 0 :
			suit =  col[1]
			#print("testpoint_2")
			#print((suit == col[1]))
		elif proceed and (suit == col[1]):
			#print (col[1])
			#print("testpoint_3")
			#print(hand)
			x=0
		else:
			proceed = False
			#print("testpoint_4")
		count = count +  1
		if (count == 5) and (proceed):
			return True

def evaluator(handOneList, handTwoList):
	rowNum = 0
	for row in handOneList:
		if isFlish(row):
			print(rowNum)
		rowNum = rowNum + 1
	rowNum = 0
	for row in handTwoList:
		if isFlish(row):
			print(rowNum)
		rowNum = rowNum + 1

#######################################
fileImporter()
evaluator(handOneList,handTwoList)

