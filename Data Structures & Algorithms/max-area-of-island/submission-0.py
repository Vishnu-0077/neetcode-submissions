class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(matrix,x,y,visited):
            count=1
            visited.add((x,y))
            n = len(matrix)
            m = len(matrix[0])
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for way in directions:
                i,j=way[0],way[1]
                xn = x+i
                yn = y+j
                if 0<=xn<n and 0<=yn<m and (xn,yn) not in visited and matrix[xn][yn]==1:
                    count = count + dfs(matrix,xn,yn,visited) #recursion logic....
            return count
                    

        def main(matrix):
            visited = set()
            ans = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]==1 and (i,j) not in visited:
                        result = dfs(matrix,i,j,visited)
                        ans = max(ans,result)
            return ans
        
        return main(grid)

        