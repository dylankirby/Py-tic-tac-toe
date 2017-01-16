board = [1,2,3,4,5,6,7,8,9]
player = 1

def print_board():
	print board[0], board[1], board[2]
	print board[3], board[4], board[5]
	print board[6], board[7], board[8]

def take_turn():
	global player
	position = input('Where would you like to place your marker?: ')
	if player == 1 and board[position] != 'O':
		board[position - 1] = 'X'
		player += 1
	elif player == 2 and board[position] != 'X':
		board[position - 1] = 'O'
		player -= 1

def check_win():
	if (
	board[0] == board[1] == board[2] or
	board[0] == board[3] == board[6] or
	board[3] == board[4] == board[5] or
	board[1] == board[4] == board[7] or
	board[6] == board[7] == board[8] or
	board[2] == board[5] == board[8] or
	board[0] == board[4] == board[8] or
	board[2] == board[4] == board[6]
	):
		return True
	else:
		return False

print 'Welcome to Tic Tac Toe, Python edition'
print 'Here is the board, numbers indicate positions'
print_board()

def run_game():
	while check_win() == False:
		take_turn()
		print_board()
	else:
		print 'Congrats player %s you win!' %(player - 1)

run_game()
