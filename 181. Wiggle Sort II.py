# https://leetcode.com/problems/wiggle-sort-ii/description/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        h=len(nums[::2])-1
        nums[::2],nums[1::2]=nums[h::-1],nums[:h:-1]