import csv

handOneList = []
handTwoList = []

def fileImporter():
#Used to import the file and prepare it for analysis.
	csvFile = open("G:\\OneDrive\\code\\project_euler\\euler_054\\p054_poker.txt", "r")
	csvReader = csv.reader(csvFile, delimiter=" ")
	row = 0
	col = 0
	for row in csvReader:
	#for each row prepare each card by seperating the two hands
		handOne = []
		handTwo = []
		counter = 0 #for spliting the hands
		for col in row:
		#put each card into its the correct hand.
			if counter < 5:
				handOne.append(makeList(col))
				#print ("handOne: ", handOne)#DEBUG
			else:
				handTwo.append(makeList(col))
				#print ("handTwo: ", handTwo)#DEBUG
			counter += 1
		#put each properly grouped hand into the correct group of hands.
		handOneList.append(handOne)
		handTwoList.append(handTwo)
	csvFile.close()

	#for row in handOneList:
		#print (row)#DEBUG
	print("#####################################")
	#for row in handTwoList:
		#print (row)#DEBUG

def makeList(str):
#Helper Function: fileImporter
#Takes a string and creates an indexable list
	list = []
	list.append(str[0])
	list.append(str[1])
	return list

def sortHand(hand):
	x = 0
	#start here	

def isFlush(hand):
#Helper Function: evaluator
#cycle through the each card in the hand and see if it matches the first card
#in the hand.
#Verified
	suit = ''
	count = 0
	proceed = True
	for col in hand:
		#print("testpoint_1")#DEBUG
		if  count == 0 :
			suit =  col[1]
			#print("testpoint_2")#DEBUG
			#print((suit == col[1]))#DEBUG
		elif proceed and (suit == col[1]):
			#print (col[1])#DEBUG
			#print("testpoint_3")#DEBUG
			#print(hand)#DEBUG
			x=0 #DEBUG
		else:
			proceed = False
			#print("testpoint_4")#DEBUG
		count = count +  1
		if (count == 5) and (proceed):
			return True

def evaluator(handOneList, handTwoList):
	rowNum = 0
	for row in handOneList:
		if isFlush(row):
			print(rowNum) #DEBUG
		rowNum = rowNum + 1
	rowNum = 0
	for row in handTwoList:
		if isFlush(row):
			print(rowNum) #DEBUG
		rowNum = rowNum + 1

#######################################
fileImporter()
evaluator(handOneList,handTwoList)

