class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            elif x == ')' and stack[-1] == '(':
                stack.pop()
            elif x == '}' and stack[-1] == '{':
                stack.pop()
            elif x == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False