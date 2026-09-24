class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final_perm = []
        def per(nums,final_perm,val=0,perm=[],perm_size = 0):
            if val==len(nums):
                final_perm.append(perm)
                return
            else:
                for i in range(perm_size+1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[val])
                    per(nums,final_perm,val+1,perm_copy,perm_size+1)
            
        per(nums,final_perm)
        return final_perm
        