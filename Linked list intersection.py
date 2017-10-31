# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:36:14 2017

@author: Zee

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = lenB = 0
        currA, currB = headA, headB
        while currA:
            lenA +=1
            currA = currA.next
        while currB:
            lenB +=1
            currB = currB.next
        currA, currB = headA, headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                currA = currA.next
        elif lenB>lenA:
            for i in range(lenB-lenA):
                currB = currB.next
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
            
        
            
