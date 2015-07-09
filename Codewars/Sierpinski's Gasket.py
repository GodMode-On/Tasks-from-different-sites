def sierpinski(n):
    rows = [['L']]
    
    for i in range(1, n + 1):
        rows_old = rows[:]
        for j, row in enumerate(rows_old):
            rows.append(row + [' '] * (len(rows_old) - j - 1) + row)
    
    return '\n'.join([' '.join(row) for row in rows])
