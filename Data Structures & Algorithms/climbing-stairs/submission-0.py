class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n):
            if n==1:
                return 1
            if n==0:
                return 1
            return rec(n-2)+rec(n-1)
        
        return rec(n)