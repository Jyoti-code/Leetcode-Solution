# https://leetcode.com/problems/closest-divisors/description/

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(int(math.sqrt(num))+1,0,-1):
            if (num+1)%i==0:
                return [i,(num+1)//i]
            if (num+2)%i==0:
                return [i,(num+2)//i]
