# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            for l,r in ranges:
                f=False
                if l <= i <=r:
                    f=True 
                    break   
            if not f:
                return False               
        return True