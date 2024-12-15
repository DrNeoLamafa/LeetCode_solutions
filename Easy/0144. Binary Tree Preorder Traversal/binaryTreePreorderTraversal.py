# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res, stack = [], [root]
        while stack:
            n = stack.pop()
            if n:
                self.res.append(n.val)
                stack.append(n.right)
                stack.append(n.left)
        return self.res

        
        