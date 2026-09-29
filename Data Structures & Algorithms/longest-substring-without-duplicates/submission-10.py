class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==' ':
            return 0
        low = 0
        high = 1
        maxi=0

        def if_uniq(s):
            p = set(s)
            if len(p)==len(s):
                return True
            return False

        while high<len(s):
            new = s[low:high]
            if if_uniq(new):
                maxi = max(maxi,len(new))
                high+=1
            elif high-low==1:
                low+=1
                high+=1
            else:
                low+=1
        return maxi
            
        
        
        