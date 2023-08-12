class Solution:
    def containsDuplicate(self, nums) -> bool:
        numbers = set()

        for n in nums:
            if n in numbers:
                return True
            else:
                numbers.add(n)
        return False