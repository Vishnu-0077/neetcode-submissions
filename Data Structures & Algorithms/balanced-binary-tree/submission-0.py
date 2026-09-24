# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left),height(root.right))

        def balance(root):
            if root is None:
                return True
            root_right = root.right
            root_left = root.left
            diff = abs(height(root_right) - height(root_left))

            if diff >1:
                return False

            return balance(root.left) and balance(root.right)
        
        return balance(root)