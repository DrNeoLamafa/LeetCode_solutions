# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        end = n
        beg = 1
        pos = 1
        while beg <= end:
            mid = beg + (end-beg)//2
            if isBadVersion(mid):
                pos = mid
                end = mid-1
            else:
                beg = mid+1
        return pos