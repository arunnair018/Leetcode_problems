s = "ccbb"
wordDict = ["bc", "cb"]

diction = sorted(wordDict,key=lambda x:len(x), reverse = True)
memo = {}

def wb(s):
    if s in memo:
        return memo[s]

    temp=s
    for word in diction:
        temp = s.replace(word," ").strip()
        if temp == s:
            continue
        if len(temp)==0 or wb(temp):
            memo[temp] = True
            return True
    memo[temp] = False
    return False

print(wb(s)) 
