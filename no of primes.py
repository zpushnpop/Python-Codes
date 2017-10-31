# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:15:00 2017

@author: Zee

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0

"""


class Solution(object):
    def countPrimes(self, n):
        primes = [True] * n
        a =[]
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        for i in range(len(primes)):
            if primes[i]:
                a.append(i)
        return a

Solution1 = Solution()
print(Solution1.countPrimes(1000))

