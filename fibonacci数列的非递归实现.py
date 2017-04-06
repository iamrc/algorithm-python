# -*- coding:utf-8 -*-
'''
斐波那切数列的非递归实现
现在要求输入一个整数n，请你输出斐波那契数列的第n项。
'''
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
return tempArray[n%2]