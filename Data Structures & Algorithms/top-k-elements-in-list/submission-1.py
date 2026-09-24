class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for x in nums:
            if x not in map:
                map[x]=1
            else:
                map[x]+=1
        
        sorted_dic = dict(sorted(map.items(),key=lambda x:x[1]))

        ans = []
        keys = list(sorted_dic.keys())
        i = 1
        while k!=0:
            ans.append(keys[-i])
            i+=1
            k-=1
        return ans

        