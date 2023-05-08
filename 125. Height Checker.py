# https://leetcode.com/problems/height-checker/description/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x=sorted(heights)
        c=0
        for i,j in zip(x,heights):
            if i!=j:
                c+=1
        return c