#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 06:47
# @Author  : Greens


"""
先来看看生活中经常遇到的事吧——假设您是个土豪，身上带了足够的1、5，11元面值的钞票。
现在您的目标是凑出某个金额w，需要用到尽量少的钞票。
"""


def main(w):
    f = []
    f.append(0)
    for i in range(1, w + 1):
        cost = i
        if i - 1 >= 0:
            cost = min(cost, f[i - 1] + 1)
        if i - 5 >= 0:
            cost = min(cost, f[i - 5] + 1)
        if i - 11 >= 0:
            cost = min(cost, f[i - 11] + 1)
        f.append(cost)
    print(f)


if __name__ == '__main__':
    main(15)
