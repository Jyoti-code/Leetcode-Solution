class Solution:
    def checkString(self, s: str) -> bool:
        j=len(s)-1
        i=0
        while i<j:
            if s[i]=='b' and s[j]=='a':
                return False
            if s[i]=='a':
                i+=1
            if s[j]=='b':
                j-=1
        return True            