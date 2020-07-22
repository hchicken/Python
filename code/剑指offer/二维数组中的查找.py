#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 16:50
# @Author  : Greens

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for my_list1 in matrix:
            for num in my_list1:
                if num == target:
                    return True
        return False

    def find(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1  # 行
        n = len(matrix[0]) - 1  # 列
        i = 0
        j = n

        # 从右上角开始找
        while i <= m and j >= 0:
            value = matrix[i][j]
            if value > target:
                j -= 1
            elif value < target:
                i += 1
            else:
                return True
        return False


if __name__ == '__main__':
    my_class = Solution()
    my_list = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    ret = my_class.find(my_list, 2)
    print(ret)
