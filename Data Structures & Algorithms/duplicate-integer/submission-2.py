class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for x in nums:
            if x not in hash_map:
                hash_map[x]=1
            else:
                return True
        return False
        