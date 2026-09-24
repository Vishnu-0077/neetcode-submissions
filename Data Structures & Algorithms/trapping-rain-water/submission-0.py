class Solution:
    def trap(self, height: List[int]) -> int:
        arr = height
        n = len(arr)
        low = 0
        high = n-1
        ans = 0
        prev_low=0
        prev_high=n-1
        while low<=high:
            if arr[low]<=arr[high]:
                if arr[low]>arr[prev_low]:
                    prev_low=low
                else:
                    ans+=abs(arr[prev_low]-arr[low])
                low+=1
            else:
                if arr[high]>arr[prev_high]:
                    prev_high=high
                else:
                    ans+=abs(arr[prev_high]-arr[high])
                high-=1
        return ans
