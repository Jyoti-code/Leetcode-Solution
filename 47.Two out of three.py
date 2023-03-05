# https://leetcode.com/problems/two-out-of-three/description/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                s.append(i)
        for j in nums2:
            if j in nums3:
                s.append(j)
        s=set(s)
        return list(s)