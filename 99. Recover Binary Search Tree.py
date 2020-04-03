# externa modue to construct binary tree
from btconstruct import ConstructTree,bfs

# Solution Start Here
def Solution(root):
    s=[]
    # Do a dfs on tree and create an array.
    def traverse(node):
        if node:
            traverse(node.left)
            s.append(node.val)
            traverse(node.right)
    traverse(root)
    # compare the array with its sorted form
    # and record the error
    err=[]
    t = sorted(s)
    for i,j in zip(s,t):
        if i!=j:
            err.append(i)
    
    # again traverse the tree and when find the 
    # error swap it.
    def recover(node):
        if node:
            recover(node.left)
            if node.val==err[0]: node.val=err[1]
            elif node.val==err[1]: node.val=err[0]
            recover(node.right)
    recover(root)

# driver code
arr = [1,3,None,None,2]
root = None
root = ConstructTree(arr,root,0,len(arr))
Solution(root)
bfs(root)
