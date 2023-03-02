class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        a=s
        for i in range(len(nums)-k):
            s-=nums[i]
            s+=nums[i+k]
            a=max(a,s)
        return a/k
	