class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isnumeric():
                stack.append(int(x))
            elif x == '+':
                stack.append(stack.pop() + stack.pop())
            elif x == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif x == '*':
                stack.append(stack.pop() * stack.pop())
            elif x == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
        return stack[0]
        