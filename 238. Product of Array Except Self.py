nums = [1,2,3,4]


def fun(nums):
    n = len(nums)
    ans = [0]*n
    left = [1]*n
    right = [1]*n

    for i in range(n-1):
        left[i+1] = nums[i]*left[i]

    for i in range(n-1,0,-1):
        right[i-1] = nums[i]*right[i]

    for i in range(n):
        ans[i] = left[i]*right[i]

    return ans

print(fun(nums))