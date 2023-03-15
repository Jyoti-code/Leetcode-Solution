# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        value=0
        for i in strs:
            if i.isdigit():
                value=max(int(i),value)
            else:
                value=max(len(i),value)
        return value