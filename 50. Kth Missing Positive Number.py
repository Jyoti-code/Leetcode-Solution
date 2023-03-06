# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=[i for i in range(0,k+len(arr)+1) if i not in arr]
        return s[k]