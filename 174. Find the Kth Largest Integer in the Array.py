# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=sorted([int(i) for i in nums])[::-1]
        return str(a[k-1])
        