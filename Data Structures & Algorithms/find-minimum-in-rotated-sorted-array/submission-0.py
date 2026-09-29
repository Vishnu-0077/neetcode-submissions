class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>=nums[low]:
                ans=nums[low]
                low=mid+1
            else:
                high=mid
        return nums[low-1]