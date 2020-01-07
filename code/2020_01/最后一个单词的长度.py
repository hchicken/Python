# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2020/1/7 21:33

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
"""


class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     s = s.strip()
    #     last_s = s.split(" ")[-1]
    #     last_len = len(last_s)
    #     return last_len

    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = 0
        for str_my in s[::-1]:
            if str_my != " ":
                i += 1
            else:
                break
        return i

if __name__ == "__main__":
    my_class = Solution()
    s = "a dasdas"
    my_def = my_class.lengthOfLastWord(s)
    print(my_def)
