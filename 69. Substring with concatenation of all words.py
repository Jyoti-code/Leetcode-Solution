# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
      maxlen=len(words)*len(words[0])
      x=[]
      for i in range(len(s)-maxlen+1):
        e=s[i:i+maxlen]
        d=[]
        for j in range(0,len(e),len(words[0])):
          d.append(e[j:j+len(words[0])])
        if sorted(d)==sorted(words):
          x.append(i)
      return x