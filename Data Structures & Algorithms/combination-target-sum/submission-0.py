class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def rec(nums,i,k):
            if k==0:
                return [[]]
            if i==len(nums):
                return []
            pick = []
            if nums[i]<=k:
                pick = [[nums[i]]+subset for subset in rec(nums,i,k-nums[i])]
            no_pick = rec(nums,i+1,k)
            return pick+no_pick
        
        return rec(nums,0,target)