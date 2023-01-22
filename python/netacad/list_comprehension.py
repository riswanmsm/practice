WHITE_PAWN = '♙'
row = [WHITE_PAWN for i in range(8)]

squares = [x ** 2 for x in range(10)]

board = []
EMPTY = ' '
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board_new = [[EMPTY for i in range(8)] for j in range(8)]

print(row, squares, board, board_new)

# determine the monthly average noon temperature
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)