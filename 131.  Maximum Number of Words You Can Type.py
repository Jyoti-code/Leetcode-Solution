# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        text=text.split()
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] in brokenLetters:
                    c-=1
                    break
            c+=1
        return c