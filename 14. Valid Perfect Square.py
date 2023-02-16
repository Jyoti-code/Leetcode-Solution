class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=int(math.sqrt(num))
        if a*a==num:
            return True
        else:
            return False