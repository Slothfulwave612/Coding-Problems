# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cpy_node = node.next
        
        node.val = cpy_node.val
        node.next = cpy_node.next
        
        cpy_node = None
        
            
        
