def minor(row, col, matrix):
    n = len(matrix)
    return [[matrix[i][j] for j in range(n) if j != col] for i in range(n) if i != row ]

def determinant(matrix):
    if len(matrix) == 1: return matrix[0][0]
    return sum([(-1) ** i * matrix[0][i] * determinant(minor(0, i, matrix)) for i in range(len(matrix))])
