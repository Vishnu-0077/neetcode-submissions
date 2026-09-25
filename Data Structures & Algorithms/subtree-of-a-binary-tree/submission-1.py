# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subtree(root,subroot):
            if ((root is not None) and (subroot is not None)) and  root.val == subroot.val:
                return subtree(root.left,subroot.left) and subtree(root.right,subroot.right)
            elif ((root is None) or (subroot is None)) and root == subroot:
                return True
            else:
                return False
        
        def traverse(root,subroot):
            if root is None:
                return False
            if root.val!=subroot.val:
                return traverse(root.left,subroot) or traverse(root.right,subroot)
            else:
                if subtree(root,subroot):
                    return True
                else:
                    return False
        
        return traverse(root,subRoot)


            