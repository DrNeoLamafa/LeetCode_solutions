class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in strs[0]:
            pref = pref + i
            bo = all(map(lambda s: s.startswith(pref), strs))
            if not bo:
                return pref[:len(pref) - 1]
        return pref