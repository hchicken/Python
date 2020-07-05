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
            q = self.partition(my_list, l, r)
            self.quit_sorte(my_list, l, q - 1)
            self.quit_sorte(my_list, q + 1, r)
        return my_list

    def partition(self, array: list, l: int, r: int) -> int:
        """
        切分
        """
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1


if __name__ == "__main__":
    my_class = Solution()
    start = time.time()
    my_list = list(range(10))
    # my_list = [4, 2, 1, 4, 8, 4, 3, 6, 7]

    my_ret = my_class.my_sorted(my_list)
    print(my_ret)
    print(time.time() - start)
