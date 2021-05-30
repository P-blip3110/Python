def swap_first_last(nums):
    temp = nums[0]
    nums[0] = nums[len(nums)-1]
    nums[len(nums)-1] = temp
    return nums

def swap_first_last2(nums):
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums

print(swap_first_last2([45, 66, 233, 55, 66, 12, 35, 9, 56, 24, 0, 90]))