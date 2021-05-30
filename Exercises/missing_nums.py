def missing_num(nums):
    missing_nums = []
    for i in range(nums[0],nums[-1]):
        if i not in nums:
            missing_nums.append(i)
    return missing_nums
    pass

print(missing_num([1, 2, 3, 7, 8]))
print(missing_num([11, 12, 13, 14, 18]))
print(missing_num([101, 102, 106, 107, 108]))