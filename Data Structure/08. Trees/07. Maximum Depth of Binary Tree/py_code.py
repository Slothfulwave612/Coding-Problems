# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        l_tree = self.maxDepth(root.left)
        r_tree = self.maxDepth(root.right)
        
        if l_tree > r_tree:
            return l_tree + 1
        else:
            return r_tree + 1
