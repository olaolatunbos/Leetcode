nums = [0,0,1,1,1,2,2,3,3,4]
l, r = 0, 1
while r < len(nums):
    if nums[l] == nums[r]:
        nums.remove(nums[l])
    l += 1
    r += 1

print(nums)

