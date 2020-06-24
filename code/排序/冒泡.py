#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 22:48
# @Author  : Greens
import time


class Solution:
    def my_sorted(self, x: list) -> list:
        """
        冒泡排序
        """
        # 遍历数组
        for i in range(len(x) - 1, -1, -1):
            # 查找出每次的最大值
            for j in range(i):
                if x[j] >= x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]
        return x


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = list(range(10000, -1, -1))
    my_ret = my_class.my_sorted(my_list)
    print(time.time() - start)
