# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        s=[]
        for i in range(left,right+1):
            a=bin(i).replace("0b","")
            x=a.count('1')
            s.append(x)
        t=[]
        for i in s:
            flag=0
            if i>1:
                for j in range(2,i):
                    if i%j==0:
                        flag=1
                        break
                if flag==0:
                    t.append(i)
        return len(t)

