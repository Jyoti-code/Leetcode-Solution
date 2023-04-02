# https://leetcode.com/problems/occurrences-after-bigram/description/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s=[]
        text=text.split()
        for i in range(len(text)-2):
            if text[i]==first and text[i+1]==second:
                s.append(text[i+2])
            else:
                continue
        return s