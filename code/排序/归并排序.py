#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 10:43
# @Author  : Greens


import time


class Solution:
    def my_sorted(self, x: list) -> list:
        """
        归并排序
        """
        list_len = len(x)
        # 设置一个退出条件
        if list_len <= 1:
            return x
        # 每次算出切割点的index
        mid = list_len // 2

        # 进行递归得出
        left = self.my_sorted(x[:mid])
        right = self.my_sorted(x[mid:])
        return self.merge(left, right)

    def merge(self, r: list, l: list) -> list:
        """
        对左右进行排序
        """
        # 定义一个ret存储中间数组
        ret = []
        i = 0
        j = 0
        # 通过while循环得到排序结果
        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                ret.append(l[j])
                j += 1
            else:
                ret.append(r[i])
                i += 1
        ret += r[i:]
        ret += l[j:]
        return ret


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = list(range(10000, -1, -1))
    # my_list = [1, 2, 3, 4, 8, 4, 5, 6, 7]

    my_ret = my_class.my_sorted(my_list)
    # print(my_ret)
    print(time.time() - start)
