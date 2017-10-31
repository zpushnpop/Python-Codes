# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:24:09 2017

@author: Zee

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i,v in enumerate(nums):
            a = target-v
            if a in nums and i!=nums.index(a):
                return [i,nums.index(a)]

Solution1 = Solution()
print(Solution1.twoSum([3,2,4], 6))