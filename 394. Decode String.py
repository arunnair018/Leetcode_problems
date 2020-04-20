s = "2[abc]3[cd]ef"

import re
from collections import Counter

#parse all values

parse = re.findall("(\d*)(\[)|([A-Za-z]*)(\])|([a-z]+)",s.strip())
parse = parse[::-1]

ans=[]
# for each value in parse
for digit,op,char1,cl,char2 in parse:
    
    # if closed brackets
    if cl:
        ans.append([])
        if char1: ans[-1].append(char1)  
    
    # if open brackets        
    if op:
        ans[-1] = ans[-1]*int(digit)
        if len(ans)>1:
        	last = ans.pop()
        	ans[-1] += last
    
    # if found letters
    if char2:
        if len(ans)>0:
        	ans[-1]+=[char2]
        else:
        	ans.append([char2])

# join all letters in list
out = ''.join(ans[0][::-1])
print(out)
