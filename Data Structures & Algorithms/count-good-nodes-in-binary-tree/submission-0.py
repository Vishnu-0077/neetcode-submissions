# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(root):
            stack = []
            stack.append(root)
            count =  0
            while stack:
                node = stack.pop(0)
                if node.left and node.right and node.val>=max(node.right.val,node.left.val):
                    count+=1
                elif node.left and node.val>=node.left.val:
                    count+=1
                elif node.right and node.val>=node.right.val:
                    count+=1
                else:
                    count+=1
                if node.left:
                    stack.append(node.left)
                elif node.right:
                    stack.append(node.right)
            return count
        
        return good(root)

        