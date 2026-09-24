class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ''
        for x in s:
            if x.isalnum():
                new+=x
        return new==new[::-1]