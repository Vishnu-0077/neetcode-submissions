class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = []
        for i in range(n):
            adj.append([])
        for pepe in edges:
            adj[pepe[0]].append(pepe[1])
            adj[pepe[1]].append(pepe[0])
        
        def dfs(adj,node,prev,visited):
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh==prev:
                    continue
                if not dfs(adj,neigh,node,visited):
                    return False
            return True
        
        node = 0
        visited = set()
        if not dfs(adj,0,-1,visited):
                return False
        for i in range(n):
            if i not in visited:
                return False
        return True

            

        