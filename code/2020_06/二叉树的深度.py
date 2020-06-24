#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 21:42
# @Author  : Greens


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # 不存在节点
        if not pRoot:
            return 0
        l_depth = self.TreeDepth(pRoot.left)  # 左边递归
        r_depth = self.TreeDepth(pRoot.right)  # 右边递归
        return max(l_depth, r_depth) + 1


if __name__ == '__main__':
    my_class = Solution()
    node = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node.left = node2
    node2.left = node3
    depth = my_class.TreeDepth(node)
    print(depth)
