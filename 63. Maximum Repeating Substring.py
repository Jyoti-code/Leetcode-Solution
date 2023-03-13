# https://leetcode.com/problems/maximum-repeating-substring/description/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        x=1
        while word*x in sequence:
            c+=1
            x+=1
        return c