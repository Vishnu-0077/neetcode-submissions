class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash1 = {}
        hash2 = {}

        for x in s:
            if x not in hash1:
                hash1[x] = 1
            else:
                hash1[x]+=1
        
        for x in t:
            if x not in hash2:
                hash2[x] = 1
            else:
                hash2[x]+=1
        
        if hash1==hash2:
            return True
        return False

        