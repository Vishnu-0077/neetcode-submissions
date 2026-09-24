class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j_value = target - nums[i]
            if j_value  in nums:
                if nums.index(j_value)!=i:
                    return sorted([i,nums.index(j_value)])
