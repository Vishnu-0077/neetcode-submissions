class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        def topo_order(n,prerequisites):
            topo = []
            for i in range(n):
                topo.append([])
            for x in prerequisites:
                topo[x[1]].append(x[0])
            return topo
        
        given = topo_order(n,prerequisites)

        ans = []
        stack = []
        for i in range(n):
            stack = []
            small_ans = []
            stack.append(i)
            while stack:
                node = stack.pop(0)
                small_ans.append(node)
                for neigh in given[node]:
                    if neigh in small_ans:
                        return False
                    stack.append(neigh)
            for p in small_ans[::-1]:
                ans.append(p)
        return True


        
            
        
            





            
        