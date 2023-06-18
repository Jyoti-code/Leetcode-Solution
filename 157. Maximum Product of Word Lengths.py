# https://leetcode.com/problems/maximum-product-of-word-lengths/description/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        c=0
        s=[set(i) for i in words]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (s[i] & s[j]):
                    c=max(c,len(words[i]*len(words[j])))
        return c

        