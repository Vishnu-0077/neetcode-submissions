# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        stack = []
        stack.append(root)
        ans = []
        while stack:
            small_ans = []
            for i in range(len(stack)):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                small_ans.append(node.val)
            ans.append(small_ans)
        
        return ans
        