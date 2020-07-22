#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 09:20
# @Author  : Greens


def binary_search(nums, item):
    l = 0  # 左边下标
    r = len(nums) - 1  # 右边下标

    while r >= l:
        mid = (l + r) // 2

        value = nums[mid]
        if value > item:
            r = mid - 1
        elif value < item:
            l = mid + 1
        else:
            return mid
    return False


if __name__ == '__main__':
    my_list = [1, 2, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
