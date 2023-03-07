# https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for i in words:
            # print(i[0])
            if s[0] == i[0] and i==s[:len(i)]:
                c+=1
        return c