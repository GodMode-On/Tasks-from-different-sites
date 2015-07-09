def sudoku(puzzle):
    nums_set = set(range(10))
    
    while not validSolution(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    if len(find_nums(puzzle, i, j)) == 9:
                        puzzle[i][j] = list(nums_set - find_nums(puzzle, i, j))[0]
    return puzzle
    
    
def validSolution(board):
    check_board = board + [[board[col][row] for col in range(9)] for row in range(9)]
    
    for i in range(3):
        for j in range(3):
            check_board.append(reduce(lambda x, y: x+y, [row[3*j:3*(j+1)] for row in board[3*i:3*(i+1)]]))
    return all([all([el.count(i) == 1 for i in range(1, 10)]) for el in check_board])
   

def find_nums(matrix, row, col):
    rr = int(row // 3)
    cc = int(col // 3)
    res = matrix[row] + [matrix[r][col] for r in range(9)] 
    return set(res + reduce(lambda x, y: x+y, [row[cc*3:3*(cc+1)] for row in matrix[3*rr:3*(rr+1)]]))
