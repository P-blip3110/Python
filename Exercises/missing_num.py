def missing_num(nums):
    for i in range(nums[0],nums[0] + len(nums)+1):
        if i not in nums:
            return i
    return None
    pass

print(missing_num([1, 2, 3, 4, 6, 7, 8]))
print(missing_num([11, 12, 13, 14, 16, 17, 18]))
print(missing_num([101, 102, 103, 104, 106, 107, 108]))