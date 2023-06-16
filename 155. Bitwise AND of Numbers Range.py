# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        a=0
        while left!=right:
            left=left>>1
            right=right>>1
            a+=1
        return right<<a

