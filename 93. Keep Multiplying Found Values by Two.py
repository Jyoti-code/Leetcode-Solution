# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in nums:
            if original in nums:
                original=2*original
        return original
