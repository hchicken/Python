#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 22:07
# @Author  : Greens


"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        my_list = array
        my_set1 = set(array)
        for i in my_set1:
            my_list.remove(i)
        my_set2 = set(my_list)

        return list(my_set1 - my_set2)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 4, 3]
    my_class = Solution()
    my_class.FindNumsAppearOnce(my_list)
