class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = "0123456789"
        conversStr = "".join(map(str.lower, filter(str.isalnum, s)))
        print(conversStr)
        if conversStr[::-1] == conversStr:
            return True
        else:
            return False