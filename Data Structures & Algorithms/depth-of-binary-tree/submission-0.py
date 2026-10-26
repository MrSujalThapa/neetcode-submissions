# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        tempmax = 0
        
        def helper(node):
            if node is None:
                return
            tempmax += 1
            helper(node.left)
            helper(node.right)
            maxi = max(tempmax, maxi)
            tempmax -= 1
        helper(root)
        return maxi
            