#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 08:27
# @Author  : Greens


"""
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,
然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？
(注：小朋友的编号是从0到n-1)
如果没有小朋友，请返回-1
"""


class Node:
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Solution:

    def make_list(self, n):
        """
        生成一个环形链表
        """
        first = None
        pre = None
        for i in range(0, n):
            new_node = Node(i)
            if i == 0:
                first = new_node
                pre = first
            else:
                pre.next = new_node
                pre = pre.next
            if i == n - 1:
                pre.next = first

        return first

    # def LastRemaining_Solution(self, n, m):
    #     """
    #     环形链表超时
    #     """
    #     if n < 1 or m < 1:
    #         return -1
    #     node = self.make_list(n)
    #     before = node
    #
    #     count = -1  # 计数器
    #     while node != node.next:
    #         count += 1
    #         if count == m - 1:
    #             count = -1
    #             before.next = node.next
    #         else:
    #             before = node
    #         node = node.next
    #     return node.item

    def LastRemaining_Solution(self, n, m):

        if n < 1 or m < 1:
            return -1
        my_list = list(range(n))
        index = 0
        while n > 1:
            index = (index + m - 1) % n
            my_list.pop(index)
            n -= 1
        return my_list[0]


if __name__ == '__main__':
    my_class = Solution()
    a = my_class.LastRemaining_Solution(41, 3)
    print(a)
