class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low = 0
        arr=nums
        high = len(nums)-1

        while low<high:
            if arr[low]+arr[high]<target:
                low+=1
            elif arr[low]+arr[high]>target:
                high-=1
            else:
                return [low,high]