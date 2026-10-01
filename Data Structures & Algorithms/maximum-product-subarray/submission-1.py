class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def rec(nums,i,state):
            if i==len(nums) and state==0:
                return 0
            if i==len(nums):
                return 1
            pick = float('-inf')
            if state<=1:
                pick = nums[i]*rec(nums,i+1,1)
            if state>=1:
                no_pick = rec(nums,i+1,2)
            else:
                no_pick = rec(nums,i+1,0)
            
            return max(pick,no_pick)
        if len(nums)==1:
            return nums[0]
        return rec(nums,0,0)