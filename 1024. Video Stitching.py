clips =  [[0,0],[9,9],[2,10],[0,3],[0,5],[3,4],[6,10],[1,2],[4,7],[5,6]]
T=5
#[[0,0],[0,3],[0,5],[1,2],[2,10],[3,4],[4,7],[5,6],[6,10],[9,9]]
clips.sort()
print(clips)
i=0
n=len(clips)
0


'''
i=0
stack=[]
clips.sort()
s = clips[0][0]
e = clips[0][1]
clip=[]     



while clips[i][0] == s:
    if clips[i][1] >= e:
        e = clips[i][1]
        clip = clips[i]
    i+=1
stack.append(clip)
while i<len(clips) and e <= T:
    if clips[i][0] <= stack[-1][1]:
        while i<len(clips) and clips[i][0] <= stack[-1][1]:
            if clips[i][1]>e:
                e = clips[i][1]
                clip = clips[i]
            i+=1
    else:
        print('-1')
        break
    stack.append(clip)
print(stack)
'''