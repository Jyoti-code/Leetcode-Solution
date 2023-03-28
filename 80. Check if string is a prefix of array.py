# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        x=[''.join(words[:i+1]) for i in range(len(words))]
        for i in x:
            if i==s:
                return True
        return False