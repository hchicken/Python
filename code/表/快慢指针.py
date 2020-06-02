#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 19:57
# @Author  : Greens


class Node:
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


node1 = Node(item=1)
node2 = Node(item=2, next=node1)
node3 = Node(item=3, next=node2)
node4 = Node(item=4, next=node3)
node5 = Node(item=5, next=node4)

fast = node5
slow = node5
while fast.next != None:
   slow=slow.next
   fast=fast.next.next

print(slow.item)