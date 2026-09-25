class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        hash = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = -(nums[i] + nums[j])
                if k in nums:
                    if k not in hash:
                        hash.add(nums[j])
                    else:
                        ans.append(sorted([nums[i],nums[j],k]))
        fin = []
        for p in ans:
            if p in fin:
                continue
            fin.append(p)
        return fin
        