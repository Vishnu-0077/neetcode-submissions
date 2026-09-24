# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_sum_path(root):
            if not root:
                return 0
            return max(root.val,root.val + max(max_sum_path(root.left),max_sum_path(root.right)))

        def multiple_path(root,maxi=root.val):
            if root is None:
                return maxi

            cur = max(root.val,root.val + max_sum_path(root.left) + max_sum_path(root.right),root.val+max(max_sum_path(root.left),max_sum_path(root.right)))
            if cur>=maxi:
                maxi=cur
            
            return max(multiple_path(root.left,maxi),multiple_path(root.right,maxi))

        return multiple_path(root)
