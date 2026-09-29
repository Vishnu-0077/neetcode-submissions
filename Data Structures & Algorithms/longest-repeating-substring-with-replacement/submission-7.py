class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_occ(s):
            low=0
            high=1
            c=1
            maxi=0
            while high<len(s):
                if s[low]==s[high]:
                    c+=1
                else:
                    low=high
                high+=1
                maxi=max(maxi,c)
            return maxi

        if not s:
            return 0
        if k==0:
            return max_occ(s)

        def pee(s,k):
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
                if low<len(s)-1 and p==0:
                    low+=1
                    prev=s[low]
                    p=k
                    c=0
            return maxi

        return max(pee(s,k),pee(s[::-1],k),pee(s[1:]+s[0],k))



        