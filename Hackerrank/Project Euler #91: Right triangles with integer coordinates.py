def prod(A, B):
    return A[0]*B[0] + A[1]*B[1]

def check_triangle(x1, x2, y1, y2):
    OX = (x1, x2)
    OY = (y1, y2)
    XY = (y1 - x1, y2 - x2)
    sides = sorted([prod(OX, OX), prod(OY, OY), prod(XY,XY)], reverse = True)
    if sides[0]  ==  sides[1] + sides[2] and not 0 in sides:
        return sides
    
n = int(input()) + 1

def right_triangles(n):
    triangles = [[x1, x2, y1, y2] for x1 in range(n) for x2 in range(n) for y1 in range(n) for y2 in range(n) if check_triangle(x1, x2, y1, y2)]
    return len(triangles) // 2                  

print (right_triangles(n))
