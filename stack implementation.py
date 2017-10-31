# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:15:15 2017

@author: Zee
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[len(self.list)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(20)
obj.push(30)

print(obj.top())
print(obj.getMin())
