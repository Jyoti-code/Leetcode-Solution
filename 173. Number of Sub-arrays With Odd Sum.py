# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        counts=[1,0]
        cur=0
        for i in arr:
            cur^=i%2
            counts[cur]+=1
        return counts[0]*counts[1]%(10**9+7)