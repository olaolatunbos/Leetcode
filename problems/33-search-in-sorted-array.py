class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l +r) // 2
            if target == nums[mid]:
                return mid
            
            # if we are in left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # target > nums[mid], goes w/o saying
                else:
                    r = mid - 1
            
            # we are in right sorted arry
            else:  
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return - 1
    
sol = Solution()

print(sol.search([4,5,6,7,0,1,2], 7))