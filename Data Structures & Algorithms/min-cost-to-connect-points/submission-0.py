class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        matrix = []
        n = len(points)
        for i in range(n):
            matrix.append([0]*n)

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i][0],points[i][1]
                x2,y2 = points[j][0],points[j][1]

                d = abs(x1-x2) + abs(y1-y2)

                matrix[i][j] = d
                matrix[j][i] = d
        
        for i in range(n):
            matrix[i][i] = float('inf')
        
        ans = 0
        i = 1
        while i<n:
            mini=min(matrix[i][:i+1])
            ans+=mini
            i+=1
        return ans








            
                
        

        