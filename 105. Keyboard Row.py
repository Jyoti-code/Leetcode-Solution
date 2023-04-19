# https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        x=[]
        for i in words:
            a=set(i.lower())
            if a<=r1 or a<=r2 or a<=r3:
                x.append(i)
        return x
