# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:55:16 2017

@author: Zee

Reversed Linked List
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.head = prev
            prev = curr
        return prev
    
    
""" Recirsive """
def reverseList(self, head, pre = None):
    if not head: return pre
    cur, head.next = head.next, pre
    return self.reverseList(cur, head)
