s= "hello"

v = ['a','e','i','o','u']
s=list(s)
stack=[]
for i in s:
    if i in v:
        stack.append(i)
for i in range(len(s)):
    if s[i] in v:
        s[i]=stack.pop()

print(''.join(s))
