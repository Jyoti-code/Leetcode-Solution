# https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        s="".join([str(i) for i in b])
        return pow(a,int(s),1337)