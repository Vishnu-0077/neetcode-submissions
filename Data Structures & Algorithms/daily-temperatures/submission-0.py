class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = (i+(temperatures[i:].index(stack[-1]))) - i
                num=0
            stack.append(temperatures[i])
        return ans

            
        