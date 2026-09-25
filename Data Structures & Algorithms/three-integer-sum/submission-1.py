class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            hash = set()
            for j in range(i+1,len(nums)):
                k = -(nums[i] + nums[j])
                if k in nums and k in hash:
                        ans.append(sorted([nums[i],nums[j],k]))
                hash.add(nums[j])
        fin = []
        for p in ans:
            if p in fin:
                continue
            fin.append(p)
        return fin
        