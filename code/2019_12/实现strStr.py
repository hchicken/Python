# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/12/31 20:37


"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle in haystack:
#             res = haystack.index(needle)
#             return res
#         else:
#             return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        len_needle = len(needle)
        len_haystack = len(haystack)
        index = 0
        while len_haystack - len_needle >= index:
            if haystack[index:index + len_needle] == needle:
                return index
            else:
                index += 1
        return -1


if __name__ == "__main__":
    my_class = Solution()
    haystack = "1"
    needle = ""
    my_def = my_class.strStr(haystack=haystack, needle=needle)
