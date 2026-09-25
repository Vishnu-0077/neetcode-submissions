class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n-1
        while low<high:
            if numbers[low]+numbers[high]<target:
                low+=1
            elif numbers[low]+numbers[high]>target:
                high-=1
            else:
                return [numbers[low],numbers[high]]