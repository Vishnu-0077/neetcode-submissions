import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        ans = []
        for i in range(n):
            ans.append(float('inf'))
        ans[k-1] = 0
        heap = []
        heapq.heappush(heap,[0,k])
        while heap:
            dist,node = heapq.heappop(heap)
            if dist>ans[node-1]:
                continue
            for x in times:
                if x[0]==node:
                    neigh = x[1]
                    new_dist = dist+x[2]
                    if new_dist<ans[neigh-1]:
                        ans[neigh-1] = new_dist
                        heapq.heappush(heap,[new_dist,neigh])
        if max(ans)==float('inf'):
            return -1
        else:
            return max(ans)
            