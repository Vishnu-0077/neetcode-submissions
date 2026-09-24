class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        areas = []
        for i in range(n):
            for j in range(i+1,n):
                areas.append(min(heights[i],heights[j])*(j-i))
        return max(areas)


        