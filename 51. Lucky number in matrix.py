# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

class Solution:
    def luckyNumbers (self, arr: List[List[int]]) -> List[int]:
        a=[]
        c=[]
        for i in range(len(arr)):
            a.append(min(arr[i]))
        for i in range(len(arr[i])):
            b=[]
            for j in range(len(arr)):
                b.append(arr[j][i])
            c.append(max(b))
        for i in a:
            for j in c:
                if i==j:
                    return [i]
        
                
