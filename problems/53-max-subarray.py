class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSub = nums[0] # can not set to zero

        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxSub = max(total, maxSub)
        return maxSub
            
        