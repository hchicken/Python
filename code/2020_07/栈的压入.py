#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 17:56
# @Author  : Greens


"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        my_list = []
        pop_index = 0
        for i in pushV:
            my_list.append(i)

            while my_list and popV[pop_index] == my_list[-1]:
                my_list.pop()
                pop_index += 1
        return not my_list


if __name__ == '__main__':
    my_class = Solution()
    my_list1 = [1, 2, 3, 4, 5]
    my_list2 = [4, 3, 5, 1, 2]
    cc = my_class.IsPopOrder(my_list1, my_list2)
    print(cc)
