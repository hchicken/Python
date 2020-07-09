#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 22:13
# @Author  : Greens


class Solution:
    def find(self, s):
        len_str = len(s)
        my_list = []
        for i in range(len_str):
            max_len_i = 1
            max_len_i1 = 0
            j = 0
            while True:
                try:
                    if s[i - j] == s[i + j]:
                        max_len_i += 2
                        j += 1
                    else:
                        break
                except:
                    break
            my_list.append(s[i - j+1: i + j])
            j = 0
            while True:
                try:
                    if s[i - j - 1] == s[i + j]:
                        max_len_i1 += 2
                        j += 1
                    else:
                        break
                except:
                    break

            my_list.append(s[i - j: i + j])
        my_list.sort(key=len)
        print(my_list[-1])


if __name__ == '__main__':
    my_class = Solution()
    s = "1212134"
    a = my_class.find(s)
    print(a)
