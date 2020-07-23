#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 08:56
# @Author  : Greens


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def lookup(root):
    """
    层序遍历
    """
    nodes = [root]
    my_list = []
    while nodes:
        node = nodes.pop()
        if node.left:
            nodes.insert(0, node.left)
        if node.right:
            nodes.insert(0, node.right)
        my_list.append(node.data)
    print(my_list)


def deep(root):
    """
    深度遍历
    """

    my_list = []
    deep1(root, my_list)
    print(my_list)
    return my_list


def deep1(root, my_list):
    """
    递归
    """
    if not root:
        return
    my_list.append(root.data)
    deep1(root.left, my_list)
    deep1(root.right, my_list)


def max_deep(root):
    """
    最大深度
    """
    if not root:
        return 0

    return max(max_deep(root.left), max_deep(root.right)) + 1


if __name__ == '__main__':
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    lookup(tree)
    deep(tree)
    mx = max_deep(tree)
    print(mx)