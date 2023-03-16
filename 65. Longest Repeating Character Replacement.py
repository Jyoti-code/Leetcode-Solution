# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=Counter()
        i=j=0
        while j<len(s):
            c[s[j]]+=1
            j+=1
            if j-i-max(c.values())>k:
                c[s[i]]-=1
                i+=1
        return j-i