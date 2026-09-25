class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        low = 0
        high = 1
        maxi = 1
        visited = set()
        visited.add(s[low])
        
        while high<len(s):
            while s[high] in visited:
                visited.remove(s[low])
                low+=1
            visited.add(s[high])
            high+=1
            maxi = max(maxi,high-low)
        return maxi

            
        
        
        