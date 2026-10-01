class Solution:
    def numDecodings(self, s: str) -> int:

        def rec(s,i,prev):
            if i==len(s):
                return 1
            pick = 0
            pick_sin=0
            if i>prev and int(s[prev:i+1])<=26:
                pick = rec(s,i+1,prev)
            if s[i]!='0':
                pick_sin = rec(s,i+1,i)
            return pick+pick_sin
        if s[0] == '0':
            return 0
        return rec(s,0,0)
        