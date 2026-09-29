# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def high(root):
            if root is None:
                return float('-inf')
            return root.val + max(high(root.left),high(root.right))

        def maxi_sum(root):
            if root is None:
                return float('-inf')
            maxi = root.val + high(root.left) + high(root.right)
            return max(maxi,maxi_sum(root.left),maxi_sum(root.right))
        
        return maxi_sum(root)