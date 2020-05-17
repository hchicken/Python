# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2020/1/6 21:51


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""

from typing import List


class Solution:
    """
    动态规划
    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_num = max(max_num, nums[i])
        return max_num


if __name__ == "__main__":
    my_class = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    my_def = my_class.maxSubArray(nums)
    print(my_def)
