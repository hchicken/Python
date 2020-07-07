#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 08:11
# @Author  : Greens


"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        my_list = []
        my_list1=[]
        my_dict = {}
        for my_str in s:
            if my_dict.get(my_str):
                my_dict[my_str] += 1
            else:
                my_list.append(my_str)
                my_dict[my_str] = 1
            my_list1.append(my_str)
        for my_str in my_list:
            if my_dict[my_str] == 1:
                return my_list1.index(my_str)

        return -1


if __name__ == '__main__':
    my_class = Solution()
    my_num = my_class.FirstNotRepeatingChar("google")
    print(my_num)
