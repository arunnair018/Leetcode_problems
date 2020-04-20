import operator
pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
pairs=sorted(pairs, key = lambda x : x[1])
b , count = float('-inf'),0
for x,y in pairs:
    if b < x:
        b = y
        count+=1
print(count)