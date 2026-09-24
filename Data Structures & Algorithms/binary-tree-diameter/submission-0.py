# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left),height(root.right))
        
        def diameter(root,max_h = None):
            if max_h is None:
                max_h = 0
            
            if root is None:
                return max_h

            root_left = root.left
            root.right = root.right

            curr_d = height(root_left) + height(root.right) 
            max_h = max(curr_d,max_h)

            return max(diameter(root.left,max_h),diameter(root.right,max_h))
        
        return diameter(root)


        