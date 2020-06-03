#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 08:04
# @Author  : Greens


"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 暴力解法
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先把所有的链表里面的数据装换成str
        str1 = []
        str2 = []
        node = ListNode(None)
        while l1:
            str1.append(str(l1.val))
            l1 = l1.next
        while l2:
            str2.append(str(l2.val))
            l2 = l2.next
        my_num = int("".join(str1[::-1])) + int("".join(str2[::-1]))
        # 遍历str后放入node
        for i in str(my_num)[::-1]:
            new_node = ListNode(int(i))
            n = node
            while n.next != None:
                n = n.next
            n.next = new_node
        node = node.next
        return node

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(None)  # 初始化一个节点
        n = node
        count = 0  # 进位数字
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = count + x + y
            count = s // 10
            n.next = ListNode(s % 10)
            n = n.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if count > 0:
            n.next = ListNode(count)
        return node.next


if __name__ == "__main__":
    my_class = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    my_class.addTwoNumbers1(node1, node1)
