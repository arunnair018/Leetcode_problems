wall= [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

def fun(wall):
    d={}
    for i in range(len(wall)):
        curr = 0
        for j in range(len(wall[i])-1):
            curr+=wall[i][j]
            print(curr)
            if curr not in d:
                d[curr]=1
            else:
                d[curr]+=1
    print(d)
    out = 0
    for x in d:
        if d[x] > out:
            out = d[x]
    
    return len(wall)-out

print(fun(wall))