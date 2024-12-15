class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = { target - i: i for i in nums}
        
        for n in nums:
            if n in dic.keys():
                f1, f2 = nums.index(n), nums.index(dic[n])
                if f1 == f2:
                        try: 
                                f2 = nums.index(dic[n], f1+1)
                                if f1 != f2:
                                        return [f1, f2]
                        except (ValueError):
                               continue
      
                else:
                        return [f1, f2]