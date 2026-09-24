class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        super_sub = []
        
        def paranthesis(n, super_n, super_sub, m=0, substr=''):
            # stop condition
            if n == 0 and m == 0:
                super_sub.append(substr)
                return
            
            # place '(' if we still have some left
            if n != 0:
                paranthesis(n-1, super_n, super_sub, m+1, substr + '(')
            
            # place ')' if there are unmatched '(' to close
            if m != 0:
                paranthesis(n, super_n, super_sub, m-1, substr + ')')
        
        paranthesis(n, n, super_sub)
        return super_sub
