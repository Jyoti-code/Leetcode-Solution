from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=Counter(nums)
        for i in n:
            if n[i]==1:
                return i