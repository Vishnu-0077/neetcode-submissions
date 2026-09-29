# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def maxi(root):
            if root is None:
                return float('-inf')
            return max(root.val,maxi(root.left),maxi(root.right))
        def mini(root):
            if root is None:
                return float('inf')
            return min(root.val,mini(root.left),mini(root.right))

        def valid(root):
            if root and root.left is None and root.right is None:
                return True
            if root is None:
                return True
            return (maxi(root.left) < root.val < mini(root.right)) and valid(root.left) and valid(root.right)
        
        return valid(root)
            
        