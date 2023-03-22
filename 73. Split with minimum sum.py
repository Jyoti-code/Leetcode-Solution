# https://leetcode.com/problems/split-with-minimum-sum/description/

class Solution:
    def splitNum(self, num: int) -> int:
        x="".join(sorted(str(num)))
        return int(x[::2])+int(x[1::2])


