# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        order = []
        while stack:
            node = stack.pop(0)
            if node is not None:
                order.append(node)
            else:
                order.append(None)
            if node is not None:
                stack.append(node.right)
                stack.append(node.left)
                nr = node.right
                node.right = node.left
                node.left = nr
        return root




        