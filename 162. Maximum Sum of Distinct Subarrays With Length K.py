# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = left = total = 0
        lookup = set()
        for right in range(len(nums)):
            while nums[right] in lookup or len(lookup) == k:
                lookup.remove(nums[left])
                total -= nums[left]
                left += 1
            lookup.add(nums[right])
            total += nums[right]
            if len(lookup) == k:
                result = max(result, total)
        return result