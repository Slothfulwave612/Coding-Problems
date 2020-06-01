# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)

            temp = root.right
            root.right = root.left
            root.left = temp
            
            return root
