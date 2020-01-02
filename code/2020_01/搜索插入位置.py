# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2020/1/2 20:33


"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
"""
from typing import List


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         len_nums = len(nums)
#         if nums[0] >= target:
#             return 0
#         for i in range(len(nums) - 1):
#             if nums[i] < target and target <= nums[i + 1]:
#                 return i + 1
#         return len_nums

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """二分查找
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 6
    my_class = Solution()
    my_def = my_class.searchInsert(nums, target)
    print(my_def)
