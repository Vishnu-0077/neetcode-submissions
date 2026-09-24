class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        c=0
        ans = []
        for x in nums:
            if x==0:
                c+=1
        for x in nums:
            total*=x
        if c<=1:
            total_0=1
            for x in nums:
                if x==0:
                    continue
                total_0*=x
            
            for x in nums:
                if x==0:
                    ans.append(total_0)
                    continue
                ans.append(total//x)
        elif c>1:
            for x in nums:
                ans.append(0)
        return ans

            


        