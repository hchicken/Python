#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 21:08
# @Author  : Greens

import time


class Solution:
    def my_sorted(self, x: list) -> list:
        """
        插入排序
        """
        list_len = len(x)
        for i in range(1, list_len):
            key = x[i]
            for j in range(i - 1, -1, -1):
                if x[j] > key:
                    x[j + 1] = x[j]
                    x[j] = key
                else:
                    break
        return x


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = [5,7,5,3,1,23]
    my_ret = my_class.my_sorted(my_list)
    print(my_ret)
    print(time.time() - start)
