# inputs and givens
board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
target = "zdz"

#solution starts here
asci = 97
alpha = {}
out = ''
start = (0,0)
end = (0,0)

# make alphabet dictionary
for i in range(5):
    for j in range(5):
        alpha[chr(asci)] = (i,j)
        asci+=1
alpha['z'] = (5,0)

# traverse through each char in target
for char in target:
    if char == 'z':
        x = start[0]-5
        y = start[1]
    else:
        end = alpha[char]
        x = start[0] - end[0]
        y = start[1] - end[1]
    if y > 0:
        out+='L'*abs(y)
    if x < 0:
        out+='D'*abs(x)
    if x > 0:
        out+='U'*abs(x)
    if y < 0:
        out+='R'*abs(y)
    out+='!'
    if char == 'z':
        start = (5,0)
    else:
        start = end

# output
print(out)