#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 20:09
# @Author  : Greens

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        tree = self.__covert(pRootOfTree)
        return tree

    def __covert(self, tree, ):
        """
        处理子节点
        """
        if not tree:
            return None
        if not tree.left and not tree.right:
            return tree
        # 左子树

        left = self.__covert(tree.left)
        p = left
        while p and p.right:
            p = p.right
        if left:
            tree.left = p
            p.right = tree

        right = self.__covert(tree.right)
        if right:
            tree.right = right
            right.left = tree

        return left if left else tree


if __name__ == '__main__':
    my_class = Solution()
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)

    tree4.left = tree2
    tree4.right = tree5

    tree2.left = tree1
    tree2.right = tree3

    my_class.Convert(tree2)
