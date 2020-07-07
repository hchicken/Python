#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 22:03
# @Author  : Greens


"""
统计一个数字在排序数组中出现的次数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):

        num = 0
        for i in data:
            if i == k:
                num += 1
            if i > k:
                break
        return num


if __name__ == '__main__':
    my_class = Solution()
    my_list = [1, 1, 1, 2, 3, 4, 5, 6, 7]
    my_class.GetNumberOfK(my_list, 1)
