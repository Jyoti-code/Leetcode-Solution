# https://leetcode.com/problems/string-matching-in-an-array/description/

class Solution:
    def stringMatching(self, arr: List[str]) -> List[str]:
        s=[]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[j] in arr[i]:
                    s.append(arr[j])
        s=set(s)
        return list(s)