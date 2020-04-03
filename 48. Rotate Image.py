# input
matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
        ]

n = len(matrix)
# Simple method transpose the matrix 
# and reverse each row. 
for i in range(n):
    for j in range(i,n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp
for row in range(len(matrix)):
    matrix[row] = matrix[row][::-1]

# pick four corners and move value
# inplace.
'''
n=len(img[0])
for x in range(n//2):# n//2 no of squares
    for y in range(x,n-x-1):  #range of column
        temp = img[x][y]    
        img[x][y] = img[n-1-y][x]           # 00 -> 30 11 -> 12
        img[n-1-y][x] = img[n-1-x][n-1-y]   # 30 -> 33 12 -> 22
        img[n-1-x][n-1-y] = img[y][n-1-x]   # 33 -> 03 22 -> 21
        img[y][n-1-x] = temp                # 03 -> 00 21 -> 11
'''
# Printing the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=' ')
    print()