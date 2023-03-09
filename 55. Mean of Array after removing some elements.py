# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr=sorted(arr)
        x=len(arr)*5//100
        return sum(arr[x:-x])/len(arr[x:-x])