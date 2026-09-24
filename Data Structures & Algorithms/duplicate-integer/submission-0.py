class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] +=1
        
        for i , j in hash.items():
            if j>1:
                return True
        return False

        