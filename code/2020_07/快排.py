#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 08:22
# @Author  : Greens


def quick_sort(nums):
    return sort1(nums, 0, len(nums) - 1)


def sort1(nums, l, r):
    if l < r:
        p = partition(nums, l, r)
        sort1(nums, l, p - 1)
        sort1(nums, p + 1, r)
    return nums

def partition(nums, l, r):
    x = nums[r]
    index = l - 1
    for i in range(l, r):

        if nums[i] < x:
            index += 1
            nums[i], nums[index] = nums[index], nums[i]
    nums[index + 1], nums[r] = nums[r], nums[index + 1]
    return index + 1


if __name__ == '__main__':
    my_list = [3, 1, 5, 8, 3, 5]
    aaa = quick_sort(my_list)
    print(aaa)
