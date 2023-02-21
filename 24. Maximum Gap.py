class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        s=[0]
        nums=sorted(nums)
        for i in range(len(nums)-1):
            a=abs(nums[i]-nums[i+1])
            s.append(a)
        return max(s)