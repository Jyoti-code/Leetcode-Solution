# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        for i in range(len(prices)):
            p=prices[i]
            d=0
            for j in range(i+1,len(prices)):
                if j>i and prices[j]<=p:
                    d=prices[j]
                    break
            s.append(p-d)
        return s