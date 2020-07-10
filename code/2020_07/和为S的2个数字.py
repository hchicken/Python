#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 08:12
# @Author  : Greens


"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        mid = 0
        mad = len(array) - 1
        while mid < mad:
            if array[mid] + array[mad] < tsum:
                mid += 1
            elif array[mid] + array[mad] > tsum:
                mad -= 1
            else:
                return array[mid], array[mad]
        return []


if __name__ == '__main__':
    my_class = Solution()
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_class.FindNumbersWithSum(my_list, 10)
