# input
paths = ["root/a 1.txt(abcd) 2.txt(efsfgh) 3.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

# Dictionary to mantain different 
# files and thier path.
dic={}
for i in paths:
    # split the path to get path and file names.
    arr = i.split(' ')
    path = arr[0]
    for i in range(1,len(arr)):
        # find the file name and its content
        content = arr[i][arr[i].find("("):]
        file = arr[i][:arr[i].find("(")]
        # joining the path and filename
        dup = path +'/'+ file
        # fill the dictionary according to content
        if content in dic:
            dic[content].append(dup)
        else:
            dic[content] = []
            dic[content].append(dup)

out = []
# if one content contain more 
# than one directory return it
for content in dic:
    if len(dic[content]) > 1:
        out.append(dic[content])

for i in out:
    print(i)                