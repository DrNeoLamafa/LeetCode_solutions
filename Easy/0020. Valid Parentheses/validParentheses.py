class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()
        for i in s:
            
            if stack and ((i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[')):
                stack.pop()
            else: stack.append(i)
        if len(stack) == 0:
            return True
        else: return False