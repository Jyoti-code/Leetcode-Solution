# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if i!=j and ((arr[i]==arr[j]+arr[j]) or (arr[i]+arr[i]==arr[j])):
                    return True
                    break
        else:
            return False