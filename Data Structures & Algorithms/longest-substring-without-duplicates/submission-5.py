class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def rec(s,i,visited,state):
            if i==len(s):
                return 0
            pick = 0
            if state!=2 and s[i] not in visited:
                visited.add(s[i])
                pick = 1+ rec(s,i+1,visited,1)
            if state>=1:
                no_pick = rec(s,i+1,set(),2)
            else:
                no_pick = rec(s,i+1,set(),0)
            return max(pick,no_pick)
        return rec(s,0,set(),0)
        
        