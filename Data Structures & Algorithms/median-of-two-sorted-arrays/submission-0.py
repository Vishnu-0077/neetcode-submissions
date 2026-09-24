class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = nums1 + nums2
        total.sort(reverse = False)
        if (m+n)%2==1:
            return total[(m+n)//2]
        else:
            return (total[(m+n)//2 - 1] + total[(m+n)//2])/2
        