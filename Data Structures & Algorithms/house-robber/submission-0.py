class Solution:
    def rob(self, nums: List[int]) -> int:

        def rec(nums,i):
            if i>=len(nums):
                return 0
            pick = nums[i] + rec(nums,i+2)
            no_pick = rec(nums,i+1)

            return max(pick,no_pick)
        
        return rec(nums,0)
        