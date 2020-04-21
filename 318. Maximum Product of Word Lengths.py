words = ["abcw","baz","foo","bar","xtfn","abcdef"]

def fun(words):
	words = sorted(words,key = lambda x : len(x),reverse=True)
	print(words)
	ans = 0
	for i in range(len(words)):
		for j in range(i,len(words)):
			if len(set(words[i]) & set(words[j])) == 0:
				ans = max(ans,len(words[i])*len(words[j])) 
	return ans

print(fun(words))