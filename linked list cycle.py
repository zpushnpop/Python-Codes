# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:34:23 2017

@author: Zee

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# My solution
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next ==None : return False
        p1, p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
            elif not p2:
                return False
    


# Fast Solution
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """         
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return true
        except:
            return false
        