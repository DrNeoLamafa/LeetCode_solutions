class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ""
        nums = ""
        for item in s:
            if item.isnumeric():
                nums = nums + item 
            elif item == " " and nums == "" and sign == "":
                continue
            elif (item == "-" or item == "+") and sign == "" and nums == "":
                sign = item
            
            else:
                break
        if nums != "":
            if sign == "-":
                nums = int(sign + nums)
            else:
                nums = int(nums)
            if nums >= 2 ** 31:
                return 2 ** 31 - 1
            elif nums <= -2 ** 31:
                return -2 ** 31 
            else:
                return nums
                
            
            
            
        else:
            return 0