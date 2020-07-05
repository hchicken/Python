#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 19:52
# @Author  : Greens


"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        nodes = [pRoot]
        keys = []
        while nodes:
            # 记录每一层的值
            curList = []

            # 记录每一层的节点
            nextLayer = []

            # 遍历每一层
            for node in nodes:
                curList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            keys.append(curList)
            nodes = nextLayer
        return keys


if __name__ == '__main__':
    my_class = Solution()
    node = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)

    node1.left = node
    node1.right = node2
    my_class.Print(node1)
