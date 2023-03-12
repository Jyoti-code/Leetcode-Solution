# https://leetcode.com/problems/letter-case-permutation/description/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        x=[S]
        for i,j in enumerate(S):
            if j.isalpha():
                x.extend([s[:i]+s[i].swapcase()+s[i+1:] for s in x])
        return x
