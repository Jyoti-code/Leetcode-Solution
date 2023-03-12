# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                return words[i]
        return ""