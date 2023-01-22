#####################################################################
# a simple program which pretends to play tic-tac-toe with the user #
#####################################################################

# random integer needed for computer to play its move
from random import randrange

# the computer (i.e., your program) should play the game using 'X's
comp_turn = 'X'

# the user (e.g., you) should play the game using 'O's;
user_turn = 'O'

# all the rows have border
row_border = '+-------+-------+-------+'

# all the columns have border
column_border = '|       |       |       |'

# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# store values 1 to 9 in a 3D list with 3 row and 3 column
# in center cell store 'X' instead of number 5
board = [[ comp_turn if j == 1 and i == 1 else (3 * j + i + 1) for i in range(3)] for j in range(3)]


# ask user to enter a value
# check the value and in the list and update the list with 0 in the place where the number is

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    for row in board:
        print(row_border)
        print(column_border)
        print('|', end = '')
        for column in row:
            print('  ', column, end = '   |')
        print('\n' + column_border)

    print(row_border)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:
        try:
            user_move = int(input('Enter your move: '))
            if user_move > 0 and user_move < 10:
                row = (user_move - 1) // len(board)
                col = (user_move - 1) % len(board)
                print(row, col)
                if board[row][col] not in ['O','X']:
                    board[row][col] = 'O'
                    break
                else:
                    print("Field already occupied - repeat your input!")
            else:
                print("Bad move - repeat your input!")
        except:
            print('Please enter an integer value between 1 and 9') 
            break
            

def make_list_of_free_fields(board):
    free = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] not in ['O', 'X']:
                free.append((i,j)) 
    return free

def victory_for(board,sgn):
	if sgn == "X":	# are we looking for X?
		who = 'me'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def draw_move(board):
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")



