class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        half = (m+n)//2 
        low = 0
        high = m
        while low<=high:
            i = (high+low)//2
            j = half - i

            nums1_left  = float('-inf') if i == 0 else nums1[i-1]
            nums1_right = float('inf')  if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j-1]
            nums2_right = float('inf') if j == n else nums2[j]

            if nums1_left<=nums2_right and nums2_left<=nums1_right:
                #correct partition
                if (m+n)%2 == 1:
                    return min(nums1_right,nums2_right)
                else:
                    return (max(nums1_left,nums2_left) + min(nums1_right,nums2_right))/2
            
            elif nums2_left>nums1_right:
                low = i+1
            else:
                high = i-1


            
            
            


            
        
        