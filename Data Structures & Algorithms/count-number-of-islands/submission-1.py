class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid,x,y,visited):
            visited.add((x,y))
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for way in directions:
                i,j = way
                xn = x+i
                yn = y+j
                if 0<=xn<len(grid) and 0<=yn<len(grid[0]) and (xn,yn) not in visited and  grid[xn][yn]=='1':
                    dfs(grid,xn,yn,visited)

        c = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in visited and grid[x][y]=='1':
                    dfs(grid,x,y,visited)
                    c+=1
        
        return c
                


        