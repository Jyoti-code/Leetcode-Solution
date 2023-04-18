# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # this pass all test cases
        k=len(s1)
        c1=Counter(s1)
        for i in range(0,len(s2)):
            if Counter(s2[i:i+k])==c1:
                return True
        return False

        # this pass 70 test cases
        # k=len(s1)
        # for i in range(0,len(s2)):
        #     if sorted(s1)==sorted(s2[i:i+k]):
        #         return True
        # return False

        # this pass 33 test cases
        # a=permutations(s1,len(s1))
        # s=[]
        # for i in list(a):
        #     s.append(''.join(i))
        # z=False
        # for i in range(0,len(s2)):
        #     if s2[i:i+len(s1)] in s:
        #         z=True
        # return z
            