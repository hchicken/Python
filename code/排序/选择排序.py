#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 23:30
# @Author  : Greens


class Solution:
    def my_sorted(self, x: list) -> list:
        my_len = len(x)
        for i in range(my_len - 1):
            # 记录下标
            min_index = i
            for j in range(i, my_len):
                # 当j小于min时跟换index
                if x[min_index] >= x[j]:
                    min_index = j
            x[min_index], x[i] = x[i], x[min_index]
        return x


if __name__ == "__main__":
    my_class = Solution()
    my_list = [4, 6, 1, 2, 9, 7, 6]
    my_ret = my_class.my_sorted(my_list)
