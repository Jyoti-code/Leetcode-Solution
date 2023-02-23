class Solution:
    def countEven(self, num: int) -> int:
        s=[]
        for i in range(2,num+1):
            a=list(str(i))
            a=sum([int(i) for i in a])
            if a%2==0:
                s.append(i)
        return len(s)