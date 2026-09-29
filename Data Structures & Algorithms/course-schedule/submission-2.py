class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def bfs(noc,org):
            for i in range(noc):
                visited = set()
                stack = []
                stack.append(i)
                while stack:
                    node = stack.pop()
                    if node in visited:
                        return False
                    visited.add(node)
                    if node not in org:
                        continue
                    for neigh in org[node]:
                        stack.append(neigh)
            return True


        org = {}
        for x,y in prerequisites:
            if y not in org:
                org[y] = [x]
            else:
                org[y].append(x)
        
        if bfs(numCourses,org):
            return True
        return False
        
        