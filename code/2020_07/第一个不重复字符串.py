#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 20:31
# @Author  : Greens


"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""


class Solution:
    def __init__(self):
        self.char = ""

    def FirstAppearingOnce(self):
        my_list = []
        my_dict = {}

        for my_str in self.char:
            if my_dict.get(my_str):
                my_dict[my_str] += 1
            else:
                my_dict[my_str] = 1
                my_list.append(my_str)
        for my_str in my_list:
            if my_dict[my_str] == 1:
                return my_str
        return "#"

    def Insert(self, char):
        self.char += char


if __name__ == '__main__':
    my_class = Solution()
    my_class.Insert("g")
    my_str = my_class.FirstAppearingOnce()
    my_class.Insert("")
    my_str = my_class.FirstAppearingOnce()
    print(my_str)
