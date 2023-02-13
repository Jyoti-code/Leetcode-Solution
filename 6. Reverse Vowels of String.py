class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        v="aeiouAEIOU"
        l=0
        h=len(s)-1
        a=""
        while l<h:
            while l<h and s[l] not in v:
                l+=1
            while h>l and s[h] not in v:
                h-=1
            s[l],s[h]=s[h],s[l]
            l+=1
            h-=1
        return "".join(s)