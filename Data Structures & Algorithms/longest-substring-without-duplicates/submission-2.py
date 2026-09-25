class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        visited = set()
        c=0
        max_c = 1
        for x in s:
            if x not in visited:
                c+=1
                visited.add(x)
            else:
                c=1
                visited=set()
            max_c = max(max_c,c)
        return max_c
        
        