class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def rec(nums,i,prev,dp):
            if i==len(nums):
                return 0
            if dp[i][prev]!=-1:
                return dp[i][prev]
            pick = 0
            if prev==-1 or nums[i]>nums[prev]:
                pick = 1 + rec(nums,i+1,i,dp)
            no_pick = rec(nums,i+1,prev,dp)

            dp[i][prev] =  max(pick,no_pick)
            return dp[i][prev]
        
        dp = [[-1]*len(nums) for i in range(len(nums))]
        return rec(nums,0,-1,dp)

