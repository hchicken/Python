#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 22:48
# @Author  : Greens


class Solution:
    def my_sorted(self, x: list) -> list:
        for i in range(len(x) - 1, -1, -1):
            for j in range(i):
                if x[j] >= x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]
        print(x)
        return x


if __name__ == "__main__":
    my_class = Solution()
    my_list = [4, 6, 1, 2, 7,6]
    my_ret = my_class.my_sorted(my_list)
