#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 16:10
# @Author  : Greens


"""

操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        l = self.Mirror(root.left)
        r = self.Mirror(root.right)
        root.left, root.right = r, l
        return root


if __name__ == '__main__':
    my_class = Solution()
    node = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node.left = node1
    node.right = node2
    node1.left = node3
    my_class.Mirror(node)
    print(node)
