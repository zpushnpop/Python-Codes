# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:24:39 2017

@author: Zee
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            c = s[i]
            if s.count(c)==i:
                return i
        return -1
            
    
    

Solution1 = Solution()
Solution1.firstUniqChar("welcome to the world of programming")

""" ^ Exeeds time limit """

class Solution2(object):
    def firstUniqChar2(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l)==1]
        return min(index) if len(index)>0 else -1
