# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        s=[0 for i in range(len(word))]
        curr=0
        for i in range(len(word)):
            curr=(curr*10+(int(word[i])))%m
            if curr==0:
                s[i]=1
        return s