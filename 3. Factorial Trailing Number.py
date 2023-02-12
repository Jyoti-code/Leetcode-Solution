class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(2,n+1):
            fact*=i
        a=str(fact)[::-1]
        c=0
        for i in a:
            if i=='0':
                c+=1
            else:
                break
        return c