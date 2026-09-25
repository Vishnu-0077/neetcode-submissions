class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for x in nums:
            total*=x
        total_0 = 1
        for x in nums:
            if x==0:
                continue
            total_0*=x
        ans = []
        for x in nums:
            if x == 0:
                ans.append(total_0)
                continue
            ans.append(total//x)
        return ans


        