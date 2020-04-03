# input
preorder = "##,5,#1" #"1,#" #"9,3,4,#,#,1,#,#,2,#,6,#,#"

# Solution starts here
# As all the null or "#" nodes are 
# leaf nodes. In a binary tree 
# leaf nodes = nodes / 2. So we use stack to 
# keep verify null nodes with non-leaf nodes.

def solution(preorder):
    stack = []
    preorder = preorder.split(',')
    
    # if preorder has only one element
    if len(preorder)<1:
        return False

    # using stack to check preorder
    # if hash comes do pop else append
    for i in preorder[:-1]:
        if i=="#":
            if not stack:
                return False
            stack.pop()
        else:
            stack.append(i)

    # if stack is empty and last item of 
    # preorder is hash than preorder is correct
    if not stack and preorder[-1]=="#":
        return True
    return False

print(solution(preorder))