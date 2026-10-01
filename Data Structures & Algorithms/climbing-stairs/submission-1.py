class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n,dp):
            if n==1:
                return 1
            if n==0:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n] =  rec(n-2,dp)+rec(n-1,dp)
            return dp[n]
        
        dp = (n+1)*[-1]
        return rec(n,dp)