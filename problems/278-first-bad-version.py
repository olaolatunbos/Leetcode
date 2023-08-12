class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            pivot = (l + r) // 2
            if isBadVersion(pivot):
                r = pivot
            else:
                l = pivot + 1
        return l