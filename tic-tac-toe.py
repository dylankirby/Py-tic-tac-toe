board = [1,2,3,4,5,6,7,8,9]
player = 1
turn_counter = 0

def print_board():
	print board[0], '|', board[1], '|', board[2]
	print '__________'
	print board[3], '|', board[4], '|', board[5]
	print '__________'
	print board[6], '|', board[7], '|', board[8]

def take_turn():
	global player
	global turn_counter
	print "Player %s, it's your turn" %(player)
	position = input('Where would you like to place your marker?: ')
	if player == 1 and board[position - 1] == position:
		board[(position - 1)] = 'X'
		player += 1
		turn_counter += 1
	elif player == 2 and board[position - 1] == position:
		board[(position - 1)] = 'O'
		player -= 1
		turn_counter += 1
	elif board[position - 1] != position:
		print 'Invalid position, try again'

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
		
# checks for a tie and returns result
def check_tie():
	if turn_counter == 9:
		print "Sorry Gents, it's a stalemate"
		reset_game()
	else:
		pass

# resets the game board if players wish to play again
def reset_game():
	play_again = raw_input('Would you like to play again? (y/n)')
	if  play_again == 'y':
		global board, turn_counter, player
		board = [1,2,3,4,5,6,7,8,9]
		turn_counter = 0
		player = 1
		run_game()
	else:
		print 'Thanks for playing'

def run_game():
	print 'Welcome to Tic Tac Toe, Python edition'
	print 'Here is the board, numbers indicate positions'
	print_board()
	while check_win() == False:
		check_tie()
		take_turn()
		print_board()
	else:
		print 'Congrats player %s you win!' %(player - 1)
		reset_game()

run_game()
