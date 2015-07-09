def neighbors(row, col, matrix):
    """returns all neighbors of the cell as a list"""
    
    n = len(matrix)
    m = len(matrix[0])
    return [matrix[r][c] for r in range(max(row - 1, 0), min(n, row + 2)) for c in range(max(col - 1, 0), min(m, col + 2)) if r != row or c != col]


def add_zero_frame(matrix):
    """adds frame of zeros around matrix"""
    
    n = len(matrix)
    m = len(matrix[0])
    res = [[0 for j in range(m+2)] for i in range(n+2)]
    
    for i in range(n+1):
        for j in range(m+1):
            if not(i == 0 or j == 0 or i == n+1 or j == m+1):
                res[i][j] = matrix[i-1][j-1]
    return res
    
    
def find_matrix(matrix):
    """finds smallest array without empty rows/colums"""
    
    min_row = len(matrix)
    min_col = len(matrix[0])
    max_row = max_col = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
                
    return [row[min_col:max_col + 1] for row in matrix[min_row:max_row + 1]]


def get_generation(cells, generations):
    start = add_zero_frame(cells) 
    
    for gen in range(generations):
        end = [row[:] for row in start[:]]
        for i in range(len(start)):
            for j in range(len(start[0])):
                neighb = sum(neighbors(i, j, start))
                if start[i][j]:
                    if  2 <= neighb <= 3:
                        end[i][j] = 1
                    else:
                        end[i][j] = 0
                else:
                    if neighb == 3:
                        end[i][j] = 1
        start = add_zero_frame(find_matrix(end))
    
    return find_matrix(start)
