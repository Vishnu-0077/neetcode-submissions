class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        full_pic = ''
        for word in wordDict:
            full_pic = full_pic+word
        for x in full_pic:
            if x not in s:
                return True
            s = s.replace(x,'')
        return False
        
        