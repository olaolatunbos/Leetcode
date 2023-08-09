class Solution:
    def twoSum(self, nums, target):
        visitedMap = {} # val : index
        output = 2 * [0]

        for i, v in enumerate(nums):
            difference = target - v
            if difference in visitedMap:
                output[0] = visitedMap[difference]
                output[1] = i
            else:
                visitedMap[v] = i
        return output