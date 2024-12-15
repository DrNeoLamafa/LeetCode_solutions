class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}
        for n in nums:
                temp.setdefault(n, 0)
                temp[n] += 1
        for k, v in temp.items():
            if v == 1:
                return k