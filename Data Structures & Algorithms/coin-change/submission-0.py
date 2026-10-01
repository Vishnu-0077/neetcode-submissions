class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def rec(coins,i,amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if i==len(coins):
                return float('inf')
            pick = float('inf')
            if coins[i]<=amount:
                pick = 1 + rec(coins,i,amount-coins[i])
            no_pick = rec(coins,i+1,amount)

            return min(pick,no_pick)
        if amount==0:
            return 0
        if rec(coins,0,amount)!=float('inf'):
            return rec(coins,0,amount)
        else:
            return -1

        