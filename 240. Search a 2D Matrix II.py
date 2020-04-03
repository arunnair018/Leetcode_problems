# input
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

# solution starts here
m = len(matrix)
n = len(matrix[0])
l = max(m,n)
i=0

while i < l:
    if matrix[i][i]==target:
        return True
    if matrix[i][i] > target:
        for k in range()