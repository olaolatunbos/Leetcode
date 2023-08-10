class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}


        for c in s:
            hashS[c] = hashS.get(c, 0) + 1

        for c in t:
            hashT[c] = hashT.get(c, 0) + 1

        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False
        return True