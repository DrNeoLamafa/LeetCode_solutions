class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start != end:
            s[start], s[end] = s[end], s[start]
            start += 1
            if start != end:
                end -= 1  