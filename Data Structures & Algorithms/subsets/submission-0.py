class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = [nums]
        n = len(nums)
        print(n)
        print(2**n)
        def rec(nums, sub,n):
            for i in range(len(nums)):
                nums_copy = nums.copy()
                nums_copy.pop(i)
                if nums_copy not in sub:
                    sub.append(nums_copy)
                print(f'added:{sub}')
                print(f'len is {len(sub)}')
                if len(sub) == 2**n:
                    return sub
                rec(nums_copy, sub,n)
            return sub
        return rec(nums,sub,n)
        