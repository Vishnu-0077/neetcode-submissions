class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if heights[i]<heights[j]:
                    ans.append(heights[i]*(j-i))
                else:
                    ans.append(heights[j]*(j-i))
        return max(ans)


        

        