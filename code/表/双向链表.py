#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 09:49
# @Author  : Greens


class Node:
    """
    定义一个双向链表节点
    """

    def __init__(self, item=None, pre=None, next=None):
        """
        pre: 上一个节点
        item: 值
        next: 下一个节点
        """
        self.pre = pre
        self.item = item
        self.next = next
