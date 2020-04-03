# input
formula = "Mg(OH)2"

formula = "K4(ON(SO3)2)2"

# solution start here
# solution one - Takes so much of memory
'''
import re
from collections import Counter
parse = re.findall('([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)',formula) 

stack=[[]]

for name,m1,o,c,m2 in parse:
    if o:
        stack.append([])
    if name:
        stack[-1].append(name * int(m1 or 1))
    if c:
        stack[-1] = stack[-1]* int(m2 or 1)
        stack[-2].extend(stack[-1])
        stack.pop()

s=''
for i in stack:
    s+=''.join(i)
s = re.findall('[A-Z][a-z]*',s)
d = dict(Counter(s))
out = ''
for i in sorted(d):
    out+=str(i)
    if d[i] != 1: 
        out+=str(d[i])
print(out)
'''
# solution two - takes less memory
import re
from collections import Counter
parse = re.findall('([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)',formula) 
stack = [Counter()]
for name, m1, o, c, m2 in parse:
    if name:
        stack[-1][name] += int(m1 or 1)
    if o:
        stack.append(Counter())
    if c:
        top = stack.pop()
        for k in top:
            stack[-1][k] += top[k] * int(m2 or 1)
out = ''
stack = dict(stack[-1])
for i in sorted(stack):
    out+=str(i)
    if stack[i] != 1: 
        out+=str(stack[i])
print(out)