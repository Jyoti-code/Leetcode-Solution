# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        n=len(pref)
        for i in words:
            if i[:n]==pref:
                c+=1
        return c