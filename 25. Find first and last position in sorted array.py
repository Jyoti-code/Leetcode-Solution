class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]!=target:
                l+=1
            elif nums[r]!=target:
                r-=1
            else:
                return [l,r]
        return [-1,-1]