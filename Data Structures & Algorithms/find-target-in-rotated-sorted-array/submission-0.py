class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[low]: #to check in which sorted place, to check insidethe left sorted array
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else: #now we are checking what if the left half is sorted then howshould be done
                if nums[mid]<target<=nums[high]:
                    low = mid +1
                else:
                    high = mid -1


        return -1

        