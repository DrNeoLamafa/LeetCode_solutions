class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        c = nums.count(0)
        if c:
            nums[:] = filter(lambda x: x != 0, nums)
            nums.extend([0 for _ in range(c)])