N = 5
dislikes = [[1,2],[3,4],[4,5],[3,5]]


def fun(N,dislikes):
    if not dislikes: return True
    graph = {}

    # graph adjacency list
    def add(n1,n2):
        if n1 in graph:
            if n2 not in graph[n1]:
                graph[n1].append(n2)
            else:
                return
        else:
            graph[n1]=[n2]
        add(n2,n1)
    # create graph        
    for i in dislikes:
        add(i[0],i[1])

    # solution starts here
    # traverse each node and color 
    # with 1 and 0. 
    color = [-1]*len(graph)
    while any(i==-1 for i in color):
        src = color.index(-1) + 1
        q = []
        q.append(src)
        color[src-1] = 1
        print(graph)
        while q:
            print(q)
            node = q.pop()
            print(node)
            # if self loop return false
            if node in graph[node]:
                return False
            # color neighbour vertice with 
            # different color
            for v in graph[node]:
                if color[v-1]== -1:
                    color[v-1] = 1 - color[node-1]
                    q.append(v)
                # if color found same return false
                elif color[v-1]==color[node-1]:
                    return False
                print(color)
    return True
    

boolvar = fun(N,dislikes)
print(boolvar)