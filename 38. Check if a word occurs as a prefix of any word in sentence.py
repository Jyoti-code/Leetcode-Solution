class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split()
        k=len(searchWord)
        for i in range(len(s)):
            if s[i][:k]==searchWord:
                return i+1
        return -1
        
