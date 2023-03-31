# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in x:
                x[s]=[i]
            else:
                x[s].append(i)
        a=[]
        for i in x.values():
            a.append(i)
        return a

        