class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        ans = []
        for x in nums:
            if x not in hash:
                hash[x] = 1
            else:
                hash[x]+=1
        sorted_items = sorted(hash.items(), key = lambda x:x[1],reverse = True)
        i = 0
        while k!=0:
            ans.append(sorted_items[i][0])
            k-=1
            i+=1
        return ans
        

        