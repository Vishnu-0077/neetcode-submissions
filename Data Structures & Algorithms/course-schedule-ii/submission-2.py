class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        def topo(n,prerequisites):
            topo = []
            for i in range(n):
                topo.append([])
            for x in prerequisites:
                topo[x[1]].append(x[0])
            return topo
        
        given = topo(n,prerequisites)

        ans = []
        visited = set()
        for i in range(n):
            stack = []
            small_ans = []
            if i not in visited:
                stack.append(i)
            while stack:
                node = stack.pop(0)
                small_ans.append(node)
                for neigh in given[node]:
                    if neigh in small_ans:
                        return []
                    if neigh not in visited:
                        stack.append(neigh)
                visited.add(node)
            for p in small_ans:
                ans.append(p)
        return ans
            
