# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            s1,s2=stones[-1],stones[-2]
            if s1==s2:
                stones.pop()
                stones.pop()
            else:
                s1=abs(s1-s2)
                stones.pop()
                print(stones)
                stones[-1]=s1
                print(stones)
        if len(stones):
            return stones[-1]
        return 0