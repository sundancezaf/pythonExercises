board = ['-', '-','-',
		 '-', '-','-',
		 '-', '-','-',]

def entireBoard():
	print(board[0] + ' | ' + board[1] + ' | ' + board[2])
	print(board[3] + ' | ' + board[4] + ' | ' + board[5])
	print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def game():
	# Winning lists
	# These lists contains the indices that need to be checked to win

	alist1 = [0,1,2]
	alist2 = [3,4,5,]
	alist3 = [6,7,8]

	alist4 = [0,3,6]
	alist5 = [1,4,7]
	alist6 = [2,5,8]

	alist7 = [2,4,6]
	alist8 = [0,4,8]


	# Need a way to be able to check all the lists at once 
	masterList = [alist1,alist2,alist3,alist4,alist5,alist6,alist7,alist8]
	# These lists will be used to check vs winning lists
	player1List = []
	player2List = []

	
	player1 = input("are you X or O?: ")
	# Establishing Xs and Os
	if player1 == 'X' or player1 =='x':
		player1 = 'X'
		player2 = 'O'
	else:
		player2 = 'X'
		player1 = 'O'

	while '-' in board:
		newChoice = input("please enter a number:")
		newChoice = int(newChoice)
		if board[newChoice-1] == '-' and board[newChoice-1]!= player2:
			player1List.append(newChoice-1)
			board[newChoice-1] = player1
			entireBoard()

	# Checking to see who is winner. Here we compare list of 
	# the players to the winning lists
		for item in range(0,8):
			if(set(masterList[item]).issubset(set(player1List))):
				return("Player 1 is winner")
			elif(set(masterList[item]).issubset(set(player2List))):
				return("Player 2 is winner")

		secondChoice = input("please enter a number:")
		secondChoice = int(secondChoice)
		if board[secondChoice-1] == '-' and board[secondChoice-1]!= player1:
			player2List.append(secondChoice-1)
			board[secondChoice-1] = player2
			entireBoard()

		for item in range(0,8):
			if(set(masterList[item]).issubset(set(player1List))):
				return("Player 1 is winner")
			elif(set(masterList[item]).issubset(set(player2List))):
				return("Player 2 is winner")
	
	print(player1List) 


print(game())
