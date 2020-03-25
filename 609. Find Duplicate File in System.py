paths = ["root/a 1.txt(abcd) 2.txt(efsfgh) 3.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

dic={}
for i in paths:
    arr = i.split(' ')
    path = arr[0]
    for i in range(1,len(arr)):
        content = arr[i][arr[i].find("("):]
        file = arr[i][:arr[i].find("(")]
        dup = path +'/'+ file
        if content in dic:
            dic[content].append(dup)
        else:
            dic[content] = []
            dic[content].append(dup)

out = []

for content in dic:
    if len(dic[content]) > 1:
        out.append(dic[content])

for i in out:
    print(i)                