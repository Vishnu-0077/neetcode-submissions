class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def rec(nums,i,prev):
            if i==len(nums):
                return 0
            pick = 0
            if prev==-1 or nums[i]>nums[prev]:
                pick = 1 + rec(nums,i+1,i)
            no_pick = rec(nums,i+1,prev)

            return max(pick,no_pick)
        
        return rec(nums,0,-1)
