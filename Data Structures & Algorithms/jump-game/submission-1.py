class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        while pos<len(nums) and nums[pos]!=0:
            pos+=nums[pos]
        
        if pos==len(nums)-1:
            return True
        return False
        