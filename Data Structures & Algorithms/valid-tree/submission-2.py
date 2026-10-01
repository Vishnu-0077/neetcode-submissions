class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = []
        for i in range(n):
            adj.append([])
        for pepe in edges:
            adj[pepe[0]].append(pepe[1])
            adj[pepe[1]].append(pepe[0])
        
        def dfs(adj,node,prev,visited):
            if node in visited and node!=prev:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh==prev:
                    continue
                if not dfs(adj,neigh,node,visited):
                    return False
            return True
        
        for i in range(n):
            visited = set()
            if not dfs(adj,i,-1,visited):
                return False
        
        return True

            

        