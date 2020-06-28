#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:14
# @Author  : Greens


"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        my_list = ListNode(None)
        node = my_list

        # 2个链表遍历直到有一个为空
        while pHead1 and pHead2:
            # val 小的加入到新链表
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
                node = node.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
                node = node.next

        # 2链表中不为空的补充到链表尾部
        if pHead1:
            node.next = pHead1
        if pHead2:
            node.next = pHead2
        return my_list.next


if __name__ == '__main__':
    my_class = Solution()
    list1 = ListNode(1)
    list1_1 = ListNode(2)
    list1_2 = ListNode(3)
    list1.next = list1_1
    list1_1.next = list1_2

    list2 = ListNode(2)
    list2_1 = ListNode(3)
    list2_2 = ListNode(4)
    list2.next = list2_1
    list2_1.next = list2_2

    node = my_class.Merge(list1, list2)
    print(node)
