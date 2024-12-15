class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[j]:
                del nums[i]
            else:
                i += 1
                j += 1