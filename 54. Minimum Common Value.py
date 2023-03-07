class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        c=list(set(nums1) & set(nums2))
        return min(c) if c else -1