class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(edges,node,visited):
            visited.add(node)
            for x in edges:
                if x[0]==node:
                    neighbour = x[1]
                    if neighbour not in visited:
                        dfs(edges,neighbour,visited)

        for i in range(len(edges)):
            edges.append([edges[i][1],edges[i][0]])
        visited = set()
        count=0
        for i in range(0,n):
            if i not in visited:
                dfs(edges,i,visited)
                count+=1
        return count
            
