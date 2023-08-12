class Solution:
    def majorityElement(self, nums):
        count, output = 0, 0

        for i in nums:
            if count == 0:
                output = i
            count += (1 if i == output else -1) 
        return output