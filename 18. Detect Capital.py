class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        words=word.upper()
        words1=word.lower()
        words2=word[0].upper()+word[1:].lower()
        if words==word:
            return True
        elif words1==word:
            return True
        elif words2==word:
            return True
        else:
            return False