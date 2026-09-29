# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def maxi(root):
            while root.right:
                root = root.right
            return root.val
        def mini(root):
            while root.left:
                root = root.left
            return root.val

        def valid(root):
            if root is None:
                return True
            elif root.left and maxi(root.left)>root.val:
                return False
            elif root.right and mini(root.right)<root.val:
                return False
            
            return valid(root.left) and valid(root.right)
        
        return valid(root)
            
        