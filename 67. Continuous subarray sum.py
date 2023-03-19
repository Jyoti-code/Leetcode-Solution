# https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem={0:-1}
        tot=0
        for i,x in enumerate(nums):
          tot+=x
          r=tot%k
          if r not in rem:
            rem[r]=i
          elif i-rem[r]>1:
            return True
        return False