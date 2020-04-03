# Function to construct graph 
def ConstructGraph(n,edges):
    graph = [[] for _ in range(n)]
    for c1, c2 in edges:
        graph[c2].append(c1)
    return graph

# Function to calculate indegree
def inorder(n,edges):
    indeg = [0] * n
    for v1, v2 in edges:
        # v2 v1 form a directed edge
        indeg[v1] += 1
    return indeg

# Function for topological sorting
def tsort(graph,indeg,n):
    count=0
    out=[]
    q = []
    # append vertice with 0 indegree 
    for v in range(n):
        if indeg[v] == 0:
            q.append(v)
    while q:
        v = q.pop(0)
        out.append(v)
        count+=1
        for i in graph[v]:
            indeg[i]-=1
            if indeg[i]==0:
                q.append(i)
    if count!=n:
        return None
    else:
        return out

# driver code
numCourses = 2
prerequisites = [[1,0],[0,1]]
graph = ConstructGraph(numCourses,prerequisites)
indeg = inorder(numCourses,prerequisites)
if tsort(graph,indeg,numCourses):
    print(True) 
else:
    print(False)