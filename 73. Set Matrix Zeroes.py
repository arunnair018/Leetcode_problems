# input

matrix = [
  [0,1,2,0],
  [3,4,0,2],
  [1,3,1,5]
]

# solution starts here
r = len(matrix)
c = len(matrix[0])

# for row and column containing 0
# mark value to None 
for i in range(r):
    for j in range(c):
        if matrix[i][j]==0:
            for k in range(r):
                if matrix[k][j] is not 0:
                    matrix[k][j] = None
            for k in range(c):
                if matrix[i][k] is not 0:
                    matrix[i][k] = None
# convert all marked values to zero.
for i in range(r):
    for j in range(c):
        if matrix[i][j]==None:
            matrix[i][j]=0

# Print Solution
for i in matrix:
    print(i)