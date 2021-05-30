def three_sum(nums):
    num_list = [[nums[i], nums[i+1], nums[i+2]] for i in range(len(nums) - 3) if nums[i] + nums[i+1] + nums[i+2] == 0]
    return num_list
    pass

print(three_sum([-1,0,1,2,-1,-4]))