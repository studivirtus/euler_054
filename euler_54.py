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
		
		#sort the lists in reverse order
		handOne.sort(reverse = True)
		handTwo.sort(reverse = True)
		
		#put each properly grouped hand into the correct group of hands.
		handOneList.append(handOne)
		handTwoList.append(handTwo)
	csvFile.close()

	for row in handOneList:
		print (row)#DEBUG
	print("#####################################")
	#for row in handTwoList:
		#print (row)#DEBUG
		
def numerize(str):
#Takes a string and makes into an int that will sort better instead of the
#mixed alpha numeric card encoding from the file.
	if is_int(str):
		return(int(str))
	elif str == 'T':
		return 10
	elif str == 'J':
		return 11
	elif str == 'Q':
		return 12
	elif str == 'K':
		return 13
	elif str == 'A':
		return 14

def is_int(i):
#modified form of:
#https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
#Changes strings to ints
    try:
        int(i)
        return True
    except ValueError:
        return False

def makeList(str):
#Helper Function: fileImporter
#Takes a string and creates an indexable list and makes the first string analysis
#integer
	list = []
	list.append(numerize(str[0]))
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

