# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:39:16 2017

@author: Zee


Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


"""

import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else: 
            return False
        

solution1 = Solution()
solution1.isAnagram("cbad", "bdca")
        
        