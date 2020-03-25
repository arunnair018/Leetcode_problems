from collections import defaultdict,Counter
class graph:

    def __init__(self,directed = False):
        self.graph = {}
        self.directed = directed
        self.vertices = set()

    def _add(self,node1,node2):
        if node1 in self.graph:
            if node2 not in self.graph[node1]:
                self.graph[node1].append(node2)
            else:
                return ;
        else:
            self.graph[node1]=[node2]

        if not self.directed:
            self._add(node2,node1)
    
    def _show_graph(self):
        print(self.graph)

    def _dfs(self,x):
        stack,path = [x],[]
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            self.vertices.add(vertex)
            if vertex in self.graph:
                for i in self.graph[vertex]:
                    stack.append(i)
        return path

accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
            ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
            ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
            ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]


g = graph()
names = {}
for acc in accounts:
    name = acc[0]
    email = acc[1:]
    names[email[0]]=name
    for mail in email[1:]:
        g._add(email[0],mail)

out=[]
for i in names.keys():
    if i not in g.vertices:
        res = g._dfs(i)
        res.sort()
        out.append([names[i]] + res)
out.sort()
print(out)
