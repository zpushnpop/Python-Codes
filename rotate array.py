# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 02:52:43 2017

@author: Zee
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        print(nums[-k:])
        print(nums[:-k])
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)
            

sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 3)