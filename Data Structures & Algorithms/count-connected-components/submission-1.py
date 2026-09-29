class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        for pee in edges:
            adj[pee[0]].append(pee[1])
            adj[pee[1]].append(pee[0])

        def dfs(adj,node,prev,visited):
            visited.add(node)
            for neigh in adj[node]:
                if neigh==prev:
                    continue
                if neigh not in visited:
                    dfs(adj,neigh,node,visited)
        c=0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(adj,i,-1,visited)
                c+=1
        return c
        