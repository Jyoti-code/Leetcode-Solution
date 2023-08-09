# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        min_diff=0
        max_diff=nums[-1]-nums[0]
        while min_diff<max_diff:
            mid_diff=(min_diff+max_diff)//2
            pair=0
            i=1
            while i<n:
                if nums[i]-nums[i-1]<=mid_diff:
                    pair+=1
                    i+=1
                i+=1
            if pair>=p:
                max_diff=mid_diff
            else:
                min_diff=mid_diff+1
        return min_diff
        # s=[]
        # nums=sorted(nums)
        # for i in range(0,len(nums)-2,2):
        #     a=abs(nums[i]-nums[i+1])
        #     print(a)
        #     s.append(a)
        # return max(s)