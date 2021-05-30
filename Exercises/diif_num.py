def is_different(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return False
    return True
    pass
def is_different_short(nums):
    if len(nums) == len(set(nums)):
        return True
    return False

print(is_different_short([1,2,3,4,5,6]))
print(is_different_short([1,2,3,4,5,6,3,1,4,1,5]))