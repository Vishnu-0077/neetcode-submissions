class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                ans=mid
                break
            elif nums[low]>target:
                low=mid+1
            elif nums[high]<target:
                high=mid-1
            
            else:
                if nums[mid]>target:
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    ans=mid
                    break
        return ans
                