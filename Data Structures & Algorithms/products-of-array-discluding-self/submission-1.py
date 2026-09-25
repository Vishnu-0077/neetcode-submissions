class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            total=1
            for y in nums:
                if y!=nums[i]:
                    total = total*y
            ans[i]=total
        return ans


        