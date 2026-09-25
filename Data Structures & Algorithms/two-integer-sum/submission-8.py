class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        low = 0
        high = len(nums)-1

        while low<high:
            if nums[low]+nums[high]<target:
                low+=1
            elif nums[low]+nums[high]>target:
                high-=1
            else:
                return [low,high]