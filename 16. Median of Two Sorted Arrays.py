class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        n=len(a)
        if n%2==1:
            return float(a[n//2])
        else:
            return (a[(n-1)//2]+a[(n-1)//2+1])/2