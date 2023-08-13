nums = [3,2,4]
target = 6

for i in nums:
    for j in nums:
        x = i + j
        if x == target:
            y, z = i, j
            break
    break

for num in range(len(nums)):
    if nums[num] == y:
        y = num
    if nums[num] == z:
        z = num
print([y, z])