# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:34:08 2017

@author: Zee

Problem definition: 
Assume you have the ability to predict prices perfectly (or equivalently, that you have the ability to go back in time and place trades). 
At each point in time, you have the option to buy a single unit, sell all units that you own, or do nothing.
 
Given a sequence of integer prices, write a function that returns a sequence of tuples of corresponding length that represents (decision, running profit), 
where decision is a char in set {B = Buy, S = Sell, N = No Action} and running profit is an integer sum of realized profit (sells minus buys).
 
Note: the function should require no more than two passes over the input sequence.
Bonus: account for the special case in which only a single pass over the input sequence is required to return the correct output.
 
 
Example

Input
1
3
2
1
 
Output
B,0
S,2
N,2
N,2


"""

class Solution(object):
    def getPprofit(self, nums):
        dict1 = {}
        profit = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dict1.update({i-1:['B',profit]})
                profit += nums[i]-nums[i-1]
                dict1.update({i:['S',profit]})
            elif nums[i]<=nums[i-1]:
                if dict1:
                    k1 = dict1.get(i-1)
                    k2 = k1[0]
                    if k2 != 'S':
                        dict1.update({i-1:['N',profit]})
                dict1.update({i:['N',profit]})
        return(dict1)
            
    
sol = Solution()
#test case 1
result = sol.getPprofit([1,3,2,1])
for i in result:
    print(result[i])
""" OUTPUT
['B', 0]
['S', 2]
['N', 2]
['N', 2]
"""
#test case 2  
result = sol.getPprofit([1,3,1,1,5,1,7,1,1,0,14])
for i in result:
    print(result[i])
""" OUTPUT
['B', 0]
['S', 2]
['N', 2]
['B', 2]
['S', 6]
['B', 6]
['S', 12]
['N', 12]
['N', 12]
['B', 12]
['S', 26]
"""    
#test case 3
result = sol.getPprofit([1,1,1,1,1,10000,10000])
for i in result:
    print(result[i])
""" OUTPUT
['N', 0]
['N', 0]
['N', 0]
['B', 0]
['S', 9999]
['N', 9999]
"""
