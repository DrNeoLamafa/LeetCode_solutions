class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        check = ""
        l1 = len(str1)
        l2 = len(str2)
        for sym in str1:
            check = check + sym
            if l1 % len(check) == 0 and l2 % len(check) == 0:
                if check * int(l1 / len(check)) == str1 and check * int(l2 / len(check)) == str2:
                    if check > res:
                        res = check

        return res

            

            