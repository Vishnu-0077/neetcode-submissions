class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low=0
        high=n-1
        while low<high:
            if nums[low]<nums[high]:
                return nums[low]
            mid = (low+high)//2     
            if nums[mid]>=nums[low]:
                low=mid+1
            else:
                high=mid

        return nums[low]
