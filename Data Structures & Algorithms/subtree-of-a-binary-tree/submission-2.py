# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ident(root1,root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            return root1.val==root2.val and ident(root1.left,root2.left) and ident(root1.right,root2.right)

        def subt(root,su):
            if root is None and su is None:
                return True
            if root is not None and su is None:
                return False
            if root is None and su is not None:
                return False
            return ident(root,su) or subt(root.left,su) or subt(root.right,su)
        
        return subt(root,subRoot)