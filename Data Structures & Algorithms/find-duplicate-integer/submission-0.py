class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = []
        for x in nums:
            if x not in l:
                l.append(x)
            else:
                return x