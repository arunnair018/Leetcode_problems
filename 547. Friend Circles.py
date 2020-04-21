
M = [[1,1,0],
     [1,1,0],
     [0,0,1]]

def fun(M):    
    circle=0 
    stack=[]
    friends = [False]*len(M)
    for i in range(len(M)):
        if not friends[i]:
            circle+=1
            stack.append(i)
            while stack:
                curr = stack.pop()
                friends[curr] = True
                for j in range(len(M)):
                    if not friends[j] and M[curr][j]==1:
                        stack.append(j)
    return circle

print(fun(M))