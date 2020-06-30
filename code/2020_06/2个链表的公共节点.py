#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 08:33
# @Author  : Greens


"""
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):

        # 临界值
        if not pHead1 or not pHead2:
            return
        l1 = pHead1
        l2 = pHead2

        # a+c+b = b+c+a l1 l2 分别遍历pHead1+pHead2 留下一个c
        while l1 != l2:
            l1 = l1.next if l1 else pHead2
            l2 = l2.next if l2 else pHead1
        return l1


if __name__ == '__main__':
    my_class = Solution()

    node1 = ListNode(11)
    node1_1 = ListNode(12)
    node1_2 = ListNode(13)

    node2 = ListNode(21)
    node2_1 = ListNode(22)

    node1.next = node1_1
    node1_1.next = node1_2

    node2.next = node2_1
    node2_1.next = node1_1

    my_class.FindFirstCommonNode(node1, node2)
