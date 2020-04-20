from collections import Counter

def fun(s,p):
    ans=[]    
    # corner case
    if len(p) > len(s): return ans
    
    # creat 2 dic using collections
    dic_p = Counter(p)
    dic_s = Counter(s[:len(p)-1])
    print(dic_s)
    print(dic_p)
    # Iterate over input s
    for i in range(len(p)-1,len(s)):
        # Add element to dic_s
        dic_s[s[i]] += 1
        
        # Check if it is anagram
        print(dic_s)
        if dic_s == dic_p:
            ans.append(i-len(p)+1)
        
        # Delete start element from dic_s
        start_element = s[i-len(p)+1]
        dic_s[start_element] -= 1
        if dic_s[start_element] == 0:
            del dic_s[start_element]   
    
    return ans

s= "cbaebabacd" 
p= "abc"
print(fun(s,p))