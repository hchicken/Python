#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 22:13
# @Author  : Greens


class Solution:
    # def find(self, s):
    #     len_str = len(s)
    #     my_list = []
    #     for i in range(len_str):
    #         max_len_i = 1
    #         max_len_i1 = 0
    #         j = 0
    #         while True:
    #             try:
    #                 if s[i - j] == s[i + j]:
    #                     max_len_i += 2
    #                     j += 1
    #                 else:
    #                     break
    #             except:
    #                 break
    #         my_list.append(s[i - j+1: i + j])
    #         j = 0
    #         while True:
    #             try:
    #                 if s[i - j - 1] == s[i + j]:
    #                     max_len_i1 += 2
    #                     j += 1
    #                 else:
    #                     break
    #             except:
    #                 break
    #
    #         my_list.append(s[i - j: i + j])
    #     my_list.sort(key=len)
    #     print(my_list[-1])

    def find(self, s):
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        max_str = ""
        # 子字符串的长度
        for l in range(n):

            for min1 in range(n):
                max1 = min1 + l
                if max1 >= n:
                    break
                # 长度为1
                if l == 0:
                    dp[min1][max1] = True
                # 长度为2
                elif l == 1:
                    dp[min1][max1] = s[min1] == s[max1]
                # 长度为其他
                else:
                    dp[min1][max1] = (dp[min1 + 1][max1 - 1] and s[min1] == s[max1])
                if dp[min1][max1] and max1 + 1 - min1 > len(max_str):
                    max_str = s[min1:max1 + 1]
        print(max_str)

if __name__ == '__main__':
    my_class = Solution()
    s = "1212134"
    a = my_class.find(s)
    print(a)
