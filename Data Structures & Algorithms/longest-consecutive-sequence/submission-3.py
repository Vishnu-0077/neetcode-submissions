class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        if len(nums) == 1:
            return 1
        nums = sorted(nums)
        ans = []
        c = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] ==1:
                c+=1
            elif nums[i+1] == nums[i]:
                continue
            else:
                ans.append(c)
                c = 1
            ans.append(c)
        ans = sorted(ans)
        if ans[-1] is None:
            return 1
        return ans[-1]
        