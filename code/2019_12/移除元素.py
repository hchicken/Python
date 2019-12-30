# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/12/30 22:21

"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                index = nums.index(val)
                del nums[index]
            except Exception as e:
                break
        res = len(nums)
        return res


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         len_nums = len(nums)
#         i = 0
#         j = 0
#         while j < len_nums:
#             if nums[j] == val:
#                 j = j + 1
#             else:
#                 nums[i] = nums[j]
#                 i = i + 1
#                 j = j + 1
#         res = len_nums - (j - i)
#         return  res


if __name__ == "__main__":
    my_class = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    my_def = my_class.removeElement(nums=nums, val=2)
