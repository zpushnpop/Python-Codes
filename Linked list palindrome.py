# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:58:08 2017

@author: Zee
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

/'-;0,lk8765t4r3e2wsertyujik+?_".0; ivcg6yftde3a2wQ1`q1w2aesrdtfygc-?|_<8vcxtz@esrdtfhjk9l0;-'=+-kojyrewQQwar4567890-\|';kreWQwsa3ZXCrt yuo.p[/|]2QWE5RT|?>
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        elif head.next == None:
            return True
            
        curr = head
        list1 = []
        i = 0
        while curr:
            list1.append(curr.val)
            curr = curr.next
        list2 = list1[::-1]
        if list1 ==list2:
            return True
        else:
            return False
            
        
            
