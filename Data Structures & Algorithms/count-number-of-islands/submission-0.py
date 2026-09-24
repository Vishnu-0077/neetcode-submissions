class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(matrix,x,y,visited):
            if (x,y) in visited:
                return
            visited.add((x,y))
            n = len(matrix)
            m = len(matrix[0])
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for way in directions:
                i,j = way[0],way[1]
                xn = x+i
                yn = y+j

                if 0<=xn<n and 0<=yn<m and (xn,yn) not in visited and matrix[xn][yn]=='1':
                    dfs(matrix,xn,yn,visited)



        def main(grid):
            visited = set()
            count = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]=='1' and (i,j) not in visited:
                        dfs(grid,i,j,visited)
                        count+=1
            return count
        return main(grid)

        