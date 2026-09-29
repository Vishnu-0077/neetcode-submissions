class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        high = 1
        p=k
        c=1
        maxi=1
        prev=s[low]
        while high<len(s):
            while high<len(s) and s[high]!=prev and p>0:
                high+=1
                p-=1
                c+=1
            while high<len(s) and s[high]==prev:
                c+=1
                high+=1
            maxi=max(maxi,c)
            if low<len(s) and p==0:
                low+=1
                prev=s[low]
                p=k
                c=0
        return maxi



        