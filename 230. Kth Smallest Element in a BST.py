# data structure for tree node
class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class bst:
    # initialize tree structure
    def __init__(self):
        self.root = None
        self.size = 0
    # insert value into the tree
    def insert(self,key):
        if key is not None:
            # if tree is empty
            if not self.root:
                self.root = node(key)
            else:
                self._insert(self.root,key)

    def _insert(self,root,key):
        # if value is greater than current node value
        if key > root.key:
            if root.right:
                self._insert(root.right,key)
            else:
                root.right = node(key)
        # if value is less than current node value
        else:
            if root.left:
                self._insert(root.left,key)
            else:
                root.left = node(key)

    # Function to find kth smalest element
    # traverse the tree and keep count when 
    # count reaches k return the value
    def kthSmallest(self, k):
        ptr = self.root
        count=[0]
        out=[]
        def traverse(ptr):
            if ptr:
                traverse(ptr.left)
                count[0]+=1
                if count[0]==k:
                    out.append(ptr.key)
                traverse(ptr.right)
        traverse(self.root)
        return out[0]

# driver code
tree_input = [5,3,6,2,4,None,None,1]
k = 3
tree = bst()
for n in tree_input:
    tree.insert(n)
print(tree.kthSmallest(k))
