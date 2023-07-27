# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1,l2=len(nums1),len(nums2)
        if not nums1 or not nums2:
            return []
        heap=[(nums1[i]+nums2[0],i,0) for i in range(l1)]
        heapq.heapify(heap)
        res=[]
        while k>0 and heap:
            s,i,j=heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
            if j+1<l2:
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
            k-=1
        return res
        # s=[]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         s.append([nums1[i],nums2[j]])
        # s=sorted(s)
        # return s[:k]
        