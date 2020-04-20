s = "TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"
n = len(s)
print(n,n/4)
from collections import Counter

def fun(s,n):
    c = Counter(s)
    print(c)

    if all(i<=n/4 for i in c.values()):
        return 0
 
    start=0
    end=0
    result = float('inf')
    for end in range(n):
        c[s[end]]-=1
        while all(j<=n/4 for j in c.values()):
            result = min(result, end-start+1)
            c[s[start]]+=1
            start+=1
        
    return result

print(fun(s,n))