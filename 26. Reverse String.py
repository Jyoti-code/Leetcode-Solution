class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s1=""
        p=0
        for i in range(0,len(s),k):
            a=""
            a=s[i:k+i]
            if p%2==0:
                a=a[::-1]
            s1=s1+a
            p+=1
        return s1