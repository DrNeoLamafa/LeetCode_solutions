class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            for n in nums2:
                for i in range(l1):
                    if nums1[i] == n:
                        res.append(n)
                        nums1[i] = ""
                        break
        else:
            for n in nums1:
                for i in range(l2):
                    if nums2[i] == n:
                        res.append(n)
                        nums2[i] = ""
                        break
        return res