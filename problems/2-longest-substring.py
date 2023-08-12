class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        substring = set()
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
            else:
                substring.remove(s[l])
                l += 1
            res = max(len(substring), res)
        return res
        