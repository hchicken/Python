#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 11:29
# @Author  : Greens

import time


class Solution:
    def my_sorted(self, x: list) -> list:
        """
        快排/
        """
        return self.quit_sorte(x, 0, len(x) - 1)

    def quit_sorte(self, my_list, l, r) -> list:
        """
        主要逻辑
        """

        if r > l:
            base = self.partition(my_list, l, r)
            self.quit_sorte(my_list, l, base - 1)
            self.quit_sorte(my_list, base + 1, r)
        return my_list

    def partition(self, my_list: list, l: int, r: int) -> list:
        """
        切分
        """

        base = my_list[l]
        while r > l:
            while r > l and my_list[r] > base:
                r -= 1
            my_list[l] = my_list[r]
            while r > l and my_list[l] <= base:
                l += 1
            my_list[r] = my_list[l]
        my_list[l] = base
        return l


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = list(range(100000, -1, -1))
    # my_list = [4, 2, 1, 4, 8, 4, 3, 6, 7]

    my_ret = my_class.my_sorted(my_list)
    # print(my_ret)
    print(time.time() - start)
