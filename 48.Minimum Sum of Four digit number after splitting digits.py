# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        arr=list(str(num))
        arr.sort()
        return int(arr[0]+arr[3])+int(arr[1]+arr[2])