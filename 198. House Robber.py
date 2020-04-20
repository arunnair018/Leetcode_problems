nums = [2,7,9,3,1]

def rob_dp_sol(nums):
    if not nums: return 0
    if len(nums)==1: return nums[0]

    prev_rob=0
    prev_not_rob=0
    curr_rob=0
    curr_not_rob=0

    for i in range(len(nums)):
        # if i rob current house
        curr_rob = prev_not_rob + nums[i]
        #if i dont rob current house 
        curr_not_rob = max(prev_rob,prev_not_rob)
        # update values
        prev_rob  = curr_rob
        prev_not_rob = curr_not_rob

    return max(prev_rob,prev_not_rob)

def rob(nums):
    if not nums: return 0
    if len(nums)==1: return nums[0]
    for i in range(len(nums)):
        # see 2 step back value
        two_back = ( nums[i-2] if i-2>=0 else 0)
        # see 3 step back value
        three_back = ( nums[i-3] if i-3>=0 else 0)
        # update curr value by adding max of above
        nums[i]+=max(two_back,three_back)
        
    return max(nums[-1],nums[-2])

print(rob_dp_sol(nums))