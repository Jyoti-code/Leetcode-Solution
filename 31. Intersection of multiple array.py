class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s=set(nums[0])
        for i in range(1,len(nums)):
            s=(s & set(nums[i]))
            print(s)
        return list(sorted(s))