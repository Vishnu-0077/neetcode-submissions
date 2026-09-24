# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def level_order(root):
            queue = []
            queue.append(root)
            order = []
            while queue:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if node is not None:
                        order.append(node.val)
                    else:
                        order.append('None')
                    if node is not None:
                        queue.append(node.left)
                        queue.append(node.right)
            print(order)
            return order
        
        if level_order(p)==level_order(q):
            return True
        else:
            return False
        