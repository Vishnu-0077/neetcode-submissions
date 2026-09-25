class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isnumeric():
                stack.append(x)
            elif x == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif x == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif x == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            elif x == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b//a)
        return stack[-1]
        