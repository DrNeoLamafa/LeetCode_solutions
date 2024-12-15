class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairStr = set()
        for i in range(len(s)):
            pairStr.add((s[i], t[i]))
        
        return len(set(s)) == len(pairStr) ==len(set(t))