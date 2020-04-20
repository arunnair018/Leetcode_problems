nums= [3,2,1]

# function to find all permutations
'''
def permutation(l):
    if len(l)==0: return []
    if len(l)==1: return [l]

    cur = []
    for i in range(len(l)):
        m = l[i]
        rem = l[:i]+l[i+1:]
        for p in permutation(rem):
            cur.append([m] + p)
    return cur

p = permutation(nums)
print(p)
'''

# solution
l = len(nums)
if l > 1:
    i,j = l-2,l-1
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    if i==-1:
        nums[:] = nums[::-1]
    else:
        while j>=0 and nums[i]>=nums[j]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:] = nums[i+1:][::-1] 

print(nums)