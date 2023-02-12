class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n1=[]
        n2=[]
        nums=[i for i in nums if i!=0]
        for i in nums:
            if i<0:
                n1.append(i)
            else:
                n2.append(i)
        return max(len(n1),len(n2))