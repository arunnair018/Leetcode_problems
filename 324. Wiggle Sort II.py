nums = [1, 5, 1, 1, 6, 4]

mid = len(nums)//2
nums.sort(reverse=True)
nums[::2],nums[1::2] = nums[mid:],nums[0:mid]
print(nums)