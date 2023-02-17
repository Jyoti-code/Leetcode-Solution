from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=Counter(nums)
        return max(s,key=s.get)