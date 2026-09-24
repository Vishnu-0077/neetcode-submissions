class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashing(s):
            char_count = {}
            for char in s:
                if char not in char_count:
                    char_count[char] = 1
                else:
                    char_count[char] += 1
            sorted_one=sorted(char_count.items())
            return ''.join([f"{k}{v}" for k, v in sorted_one])
        
        if len(s) != len(t):
            return False
        if hashing(s) == hashing(t):
            return True

        return False
        