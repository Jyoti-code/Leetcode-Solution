class Solution:
    def sumOfUnique(self, n: List[int]) -> int:
        s=[]
        for i in n:
            if n.count(i)==1:
                s.append(i)
        return sum(s)