# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            i=s.index(part)
            s=s[:i]+s[i+len(part):]
        return s      