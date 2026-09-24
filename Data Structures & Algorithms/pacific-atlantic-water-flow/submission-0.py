class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs_pacific(matrix,x,y,visited,pacific,atlantic):
            if (x,y) in atlantic:
                return True
            visited.add((x,y))
            n = len(matrix)
            m = len(matrix[0])
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for way in directions:
                i,j = way[0],way[1]
                xn = x+i
                yn = y+j
                if 0<=xn<n and 0<=yn<m and (xn,yn) not in visited and matrix[xn][yn]<=matrix[x][y]:
                    if dfs_pacific(matrix,xn,yn,visited,pacific,atlantic):
                        return True
        
        def dfs_atlantic(matrix,x,y,visited,pacific,atlantic):
            if (x,y) in pacific:
                return True
            visited.add((x,y))
            n = len(matrix)
            m = len(matrix[0])
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for way in directions:
                i,j = way[0],way[1]
                xn = x+i
                yn = y+j
                if 0<=xn<n and 0<=yn<m and (xn,yn) not in visited and matrix[xn][yn]<=matrix[x][y]:
                    if dfs_atlantic(matrix,xn,yn,visited,pacific,atlantic):
                        return True

        pacific_1 = [(0,m) for m in range(len(heights[0]))]
        pacific_2 = [(n,0) for n in range(len(heights))]
        pacific = pacific_1 + pacific_2

        atlantic_1 = [(len(heights)-1,m) for m in range(len(heights[0]))]
        atlantic_2 = [(n,len(heights[0])-1) for n in range(len(heights))]
        atlantic = atlantic_1 + atlantic_2

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = set()
                    
                if (i,j) in pacific and (i,j) not in atlantic:
                    Flag1 = True
                    Flag2 = False

                    if dfs_pacific(heights,i,j,visited,pacific,atlantic):
                        Flag2 = True
                    
                elif (i,j) not in pacific and (i,j) in atlantic:
                    Flag1=False
                    Flag2=True

                    if dfs_atlantic(heights,i,j,visited,pacific,atlantic):
                        Flag1 = True
                    
                else:
                    Flag1 = False
                    Flag2 = False

                    if dfs_pacific(heights,i,j,visited,pacific,atlantic) and dfs_atlantic(heights,i,j,set(),pacific,atlantic):
                        Flag1 = True
                        Flag2 = True
                    
                if Flag1 and Flag2:
                    ans.append([i,j])
        return ans