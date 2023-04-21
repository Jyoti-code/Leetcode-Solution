# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        x=['a','b','c','d','e','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        a=''
        b=''
        c=''
        for i in firstWord:
            a+=str(x.index(i))
        for i in secondWord:
            b+=str(x.index(i))
        for i in targetWord:
            c+=str(x.index(i))
        if int(a)+int(b)==int(c):
            return True
        else:
            return False
        