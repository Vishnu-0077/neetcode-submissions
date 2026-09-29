class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def bfs(noc,org):
            for i in range(noc):
                stack = []
                stack.append([i,set()])
                while stack:
                    node,path = stack.pop()
                    if node in path:
                        return False
                    new_path = path.copy()
                    new_path.add(node)
                    if node not in org:
                        continue
                    for neigh in org[node]:
                        stack.append([neigh,new_path])
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
        
        