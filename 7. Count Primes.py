class Solution:
    def countPrimes(self, n: int) -> int:
        p=[0,0]+[1]*(n-2)
        for i in range(2,int(sqrt(n))+1):
            if p[i]==1:
                for j in range(i*i,n,i):
                    p[j]=0
        return sum(p)