#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 16:26
# @Author  : Greens


"""
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

"""


class Solution:
    # def findRepeatNumber(self, nums) -> int:
    #     nums_len = len(nums)
    #     for i in range(nums_len):
    #         i1 = nums.index(nums[i])
    #         if i1 != i:
    #             return nums[i]
    #     return 0

    def findRepeatNumber(self, nums) -> int:
        nums_len = len(nums)
        my_dict = {}
        for i in range(nums_len):
            num = my_dict.get(nums[i], "")
            if num != "":
                return nums[i]
            my_dict[nums[i]] = i
        return 0


if __name__ == '__main__':
    my_class = Solution()
    my_list = [2, 3, 1, 0, 2, 5, 3]
    num = my_class.findRepeatNumber(my_list)
    print(num)
