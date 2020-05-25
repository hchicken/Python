#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 20:22
# @Author  : Greens

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


# class Solution:
#     # 递归：容易内存溢出
#     def climbStairs(self, n: int) -> int:
#         if n <= 1:
#             return 1
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# class Solution:
#     def __init__(self):
#         self.my_list = []
#
#     # 记忆化递归
#     def add(self, n: int) -> int:
#         if n <= 1:
#             return 1
#         if len(self.my_list) > n - 2:
#             return self.my_list[n - 2]
#         num = self.add(n - 1) + self.add(n - 2)
#         # 第一个存进my_list时n为2
#         self.my_list.append(num)
#         return num
#
#     def climbStairs(self, n: int) -> int:
#         return self.add(n)


class Solution:
    # 迭代
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        num1 = 1
        num2 = 1
        for i in range(1, n):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num2


if __name__ == "__main__":
    my_int = 2
    my_class = Solution()
    my_def = my_class.climbStairs(my_int)
    print(my_def)
