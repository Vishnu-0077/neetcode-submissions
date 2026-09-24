class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        def product(arr):
            if len(arr) == 0:
                return 1
            return arr[0]*product(arr[1:])

        for i in range(len(nums)):
            copy_nums = nums.copy()
            copy_nums.remove(nums[i])
            ans.append(product(copy_nums))
        return ans
            
        