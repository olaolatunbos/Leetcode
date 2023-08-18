class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l +=1
            elif nums[i] == 2: # if we encounter 2 we swap but do not increment i
                swap(i, r)
                r -= 1
                i -= 1
            i += 1