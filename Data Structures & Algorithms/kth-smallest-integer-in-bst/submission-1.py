# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def nos(root):
            if root is None:
                return 0
            return 1 + nos(root.left) + nos(root.right)
        
        while root:
            if k==nos(root.left)+1:
                return root.val
                break
            elif k>nos(root.left)+1:
                k = k-(nos(root.left)+1)
                root=root.right
                continue
            else:
                root=root.left
                continue
        
        return -1
        