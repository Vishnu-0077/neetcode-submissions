class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(coins,i,amount,dp):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if i==len(coins):
                return float('inf')
            if dp[i][amount]!=-1:
                return dp[i][amount]
            pick = float('inf')
            if coins[i]<=amount:
                pick = 1 + rec(coins,i,amount-coins[i],dp)
            no_pick = rec(coins,i+1,amount,dp)

            dp[i][amount] = min(pick,no_pick)
            return dp[i][amount]
        if amount==0:
            return 0
        
        dp = [[-1]*(amount+1) for i in range(len(coins))]
        if rec(coins,0,amount,dp)!=float('inf'):
            return rec(coins,0,amount,dp)
        else:
            return -1

        