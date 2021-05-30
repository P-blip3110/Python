def sum13(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 13:
      nums[i] = 0
      nums[i + 1] = 0
  if nums[-1] == 13:
      nums.pop()
  return sum(nums)


print(sum13([13, 1, 2, 2, 13]))