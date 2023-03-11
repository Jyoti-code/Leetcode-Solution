# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # Brute force TLE solution
        # x=[]
        # for i in range(len(nums)):
        #     s=[]
        #     for j in range(len(nums)):
        #         a=abs(nums[i]-nums[j])
        #         s.append(a)
        #     x.append(sum(s))
        # return x
        left_sum, right_sum = 0, sum(nums)
        left, right = 0, len(nums)
        res = []
        for i in nums:
            res.append((i*left - left_sum) + (right_sum - i*right))
            left += 1
            right -= 1
            left_sum += i
            right_sum -= i
        return res
        