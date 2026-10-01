class Solution:
    def rob(self, nums: List[int]) -> int:

        def rec(nums,i,dp):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick = nums[i] + rec(nums,i+2,dp)
            no_pick = rec(nums,i+1,dp)

            dp[i] =  max(pick,no_pick)
            return dp[i]
        dp = [-1]*len(nums)
        return rec(nums,0,dp)
        