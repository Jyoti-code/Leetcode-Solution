class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s+=str(i)
        a=int(s)+k
        return [int(i) for i in str(a)]
        