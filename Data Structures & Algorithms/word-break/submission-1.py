class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        full = ''
        for word in wordDict:
            full = full+word

        def lcs(s,full):
            n = len(s)
            m = len(full)
            dp = [[0]*m for i in range(n)]
            
            for i in range(m):
                if s[0]==full[i]:
                    dp[0][i]=1
                else:
                    dp[0][i]=dp[0][i-1]
            
            for i in range(n):
                if full[0]==s[i]:
                    dp[i][0]=1
                else:
                    dp[i][0]=dp[i-1][0]
            
            for i in range(1,n):
                for j in range(1,m):
                    if s[i]==full[j]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
            return dp[n-1][m-1]
        
        val = lcs(s,full)
        if len(full)==val:
            return True
        return False