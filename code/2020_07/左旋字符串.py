#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 07:55
# @Author  : Greens


"""
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    def LeftRotateString(self, s, n):
        if s == "" or n <= 0:
            return s
        my_list = []
        for my_str in s:
            my_list.append(my_str)
        for i in range(0, n):
            a = my_list.pop(0)
            my_list.append(a)

        return "".join(my_list)


if __name__ == '__main__':
    my_class = Solution()
    my_str = "XYZdefabc"
    my_num = 3
    my_class.LeftRotateString(my_str, my_num)
