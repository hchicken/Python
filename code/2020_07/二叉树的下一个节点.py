#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 17:30
# @Author  : Greens


"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return

        # 存在右子节点,则下一个节点为
        if pNode.right:
            next = pNode.right
            while next.left:
                next = next.left
            return next

        while pNode.next:
            # 该节点为父节点的左子节点
            if pNode == pNode.next.left:
                return pNode.next
            pNode = pNode.next


if __name__ == '__main__':
    pass
