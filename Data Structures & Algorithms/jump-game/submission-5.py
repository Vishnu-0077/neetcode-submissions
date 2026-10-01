class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        while pos<len(nums)-1 and nums[pos]!=0:
            if pos+nums[pos]>=len(nums):
                return True
            pos+=nums[pos]
        if pos==len(nums)-1:
            return True
        return False
        