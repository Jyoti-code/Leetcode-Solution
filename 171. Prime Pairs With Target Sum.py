# https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans=[]
        prime=[0,0]+[1]*n
        s=int(sqrt(n))
        for i in range(2,s+1):
            if prime[i]:
                for j in range(i+i,n+1,i):
                    prime[j]=0
        for i in range(2,n//2+1):
            if prime[i] and prime[n-i]:
                ans.append([i,n-i])
        return ans
