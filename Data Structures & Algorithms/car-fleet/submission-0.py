class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        pair.sort(reverse = True)
        for p,s in pair:
            time = (target-p)/s
            if stack and stack[-1]>=time:
                stack.pop()
            stack.append(time)
        return len(stack)




        