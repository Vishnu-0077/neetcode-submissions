class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        while nums[pos]!=0 and pos<len(nums):
            pos+=nums[pos]
        
        if pos==len(nums)-1:
            return True
        return False
        