# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left:
                root.right = root.left
                root.left = None
            elif root.right:
                root.left = root.right
                root.right = None
            if root.left:
                invert(root.left)
            if root.right:
                invert(root.right)
        if root:
            invert(root)
        return root
        