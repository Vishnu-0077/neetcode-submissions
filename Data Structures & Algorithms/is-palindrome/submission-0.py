class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace('?',' ',)
        s = s.strip()
        lst = s.split()
        s = ''.join(lst)
        if s == s[::-1]:
            return True
        return False