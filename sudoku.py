import numpy as np
'''
# Thanks for Tim for this great solution. 
# I'm sharing this one who would like to play.
# There are some other solutions however
# they look like O(Scary) rather than O(N^2) or O(N^3)
'''
board = [[0,0,0,7,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[0,0,0,4,3,0,2,0,0],
[0,0,3,0,0,0,0,0,6],
[0,0,0,5,0,9,0,0,0],
[0,0,0,0,0,0,4,1,8],
[0,0,0,0,8,1,0,0,0],
[0,8,2,0,0,0,0,5,0],
[0,4,0,0,0,7,3,0,0]
]

Extreme_Memory_Consumption_Be_Careful = [
[0,0,0,7,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[0,0,0,4,3,0,2,0,0],
[0,0,0,0,0,0,0,0,6],
[0,0,0,5,0,9,0,0,0],
[0,0,0,0,0,0,4,1,8],
[0,0,0,0,8,1,0,0,0],
[0,0,2,0,0,0,0,5,0],
[0,4,0,0,0,0,3,0,0]
]

print(np.matrix(board))

def find_empty(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) # row, column
    return None

def is_valid(board, num, pos):

    # Compare all numbers in the Row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Compare all numbers in the column    
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Compare all numbers in the cubes

    x0 = pos[1] // 3
    y0 = pos[0] // 3

    for i in range(y0 * 3, y0 * 3 + 3):
        for j in range(x0 * 3, x0 * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve_it(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            # call the solve_it method from inside itself
            # to continue until it returns True 
            if solve_it(board):
                return True
            board[row][col] = 0

    return False

print(np.matrix(board))
solve_it(board)
print('\n___________________________\n')
print(np.matrix(board))