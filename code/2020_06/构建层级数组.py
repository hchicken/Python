#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 19:42
# @Author  : Greens


"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
"""


class Solution:
    def multiply(self, A):
        # write code here

        list_B = []

        len_a = len(A)
        for i in range(len_a):
            sum = 1
            for j in A[:i] + A[i + 1:]:
                sum *= j
            list_B.append(sum)
        return list_B


if __name__ == "__main__":
    my_class = Solution()
    list_A = [1, 2, 3, 4, 5]
    my_class.multiply(list_A)
