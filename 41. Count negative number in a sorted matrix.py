class Solution:
    def countNegatives(self, arr: List[List[int]]) -> int:
        c=0
        for ele in range(len(arr)):
            for i in range(len(arr[ele])):
                if arr[ele][i]<0:
                    c+=1
        return c