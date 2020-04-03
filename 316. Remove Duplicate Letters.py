# input
s = 'ecbacba'

# Solution starts here
from collections import Counter

stack=[]
visited = set()
count = Counter(s)
# travesrse one byb one in string
for i in s:
    # decrement count from dictionary
    count[i] -= 1
    if i not in visited:
        while stack:
            # if the element is less than last element of 
            # stack and the last elements of stack has 
            # count greater than zero pop from stack 
            # and unmark visited
            if i < stack[-1] and count[stack[-1]] > 0:
                x = stack.pop()
                visited.remove(x)
            else:
                break
        # put element in stack and mark visited
        stack.append(i)
        visited.add(i)
# return the stack for lexographically non repeating order
print(''.join(stack))
