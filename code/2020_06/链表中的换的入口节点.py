#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:38
# @Author  : Greens


"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead.next or not pHead.next.next:
            return None
        slow = pHead.next
        fast = pHead.next.next
        while fast:
            if fast == slow:
                fast = pHead
                while (fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast
            slow = slow.next
            fast = fast.next.next
        return None


if __name__ == '__main__':
    node = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    my_class = Solution()
    a = my_class.EntryNodeOfLoop(node)
    print(a)
