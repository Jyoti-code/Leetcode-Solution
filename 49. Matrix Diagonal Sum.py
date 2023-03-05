# https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s1=0
        s2=0
        a=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j and (i+j)==len(mat)-1:
                    a=mat[i][j]
                    # print(a)
                if i==j:
                    s1+=mat[i][j]
                if (i+j)==len(mat)-1:
                    s2+=mat[i][j]
        return (s1+s2)-a