# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def count(root):
            if root is None:
                return 0
            return 1+count(root.left)+count(root.right)
        
        def count_left(root):
            if root is None:
                return 0
            return 1+count(root.left)
        def small(root,k):

            while root:
                if count_left(root)==k:
                    return root.val
                elif count_left(root)>k:
                    root=root.left
                elif count_left(root)<k:
                    k=k-count_left(root)
                    root = root.right
            return root.val
        
        return small(root,k)

        