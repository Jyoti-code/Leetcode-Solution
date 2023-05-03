# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        return [i for i,j in x.most_common(k)]