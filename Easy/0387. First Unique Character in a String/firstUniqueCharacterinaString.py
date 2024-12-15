import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        cound = collections.Counter(s)
        count = list(filter(lambda x: cound[x] == 1, cound.keys()))
        if count:
            return s.find(count[0])
        else:
            return -1