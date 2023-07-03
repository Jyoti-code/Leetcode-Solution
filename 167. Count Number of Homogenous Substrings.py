# https://leetcode.com/problems/count-number-of-homogenous-substrings/description/

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for c, s in groupby(s):
            # print(c,list(s))
            n = len(list(s))
            res += n * (n + 1) // 2
        return res % (10**9 + 7)