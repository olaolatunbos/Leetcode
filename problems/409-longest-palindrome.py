from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashRansom, hashMagazine = Counter(ransomNote), Counter(magazine)
        
        for c in hashRansom:
            if hashRansom[c] > hashMagazine.get(c, 0):
                return False
        return True
        