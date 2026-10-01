class Solution:
    def rob(self, nums: List[int]) -> int:

        first_nums = nums[:-1]
        second_nums = nums[1:]

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
        dp_1 = dp.copy()
        if len(nums)==1:
            return nums[0]
        return max(rec(first_nums,0,dp),rec(second_nums,0,dp_1))


        