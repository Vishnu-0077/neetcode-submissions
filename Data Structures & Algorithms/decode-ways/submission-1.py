class Solution:
    def numDecodings(self, s: str) -> int:

        def rec(s,i,prev,dp):
            if i==len(s):
                return 1
            pick = 0
            pick_sin=0
            if dp[i][prev]!=-1:
                return dp[i][prev]
            if i>prev and int(s[prev:i+1])<=26:
                pick = rec(s,i+1,prev,dp)
            if s[i]!='0':
                pick_sin = rec(s,i+1,i,dp)
            dp[i][prev] = pick+pick_sin
            return dp[i][prev]
        if s[0] == '0':
            return 0
        
        dp = [[-1]*len(s) for i in range(len(s))]
        return rec(s,0,0,dp)
        