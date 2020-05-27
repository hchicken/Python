#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 21:45
# @Author  : Greens

import time


class Solution:
    def my_sorted(self, x: list) -> list:
        list_len = len(x)
        # 根据数组长度获取h的初始值
        h = 1
        while h < list_len / 2:
            h = 2 * h + 1
        # 开始分组排序
        while h >= 1:
            # 排序
            # 从h开始增加
            for i in range(h, list_len):
                # 需要排序的元素
                key = x[i]
                # 对元素进行比较替换位子
                for j in range(i - h, -1, -h):
                    if x[j] > key:
                        x[j + h] = x[j]
                        x[j] = key
                    else:
                        break
            h = h // 2
        return x


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = list(range(100000, -1, -1))
    my_ret = my_class.my_sorted(my_list)
    print(time.time() - start)
