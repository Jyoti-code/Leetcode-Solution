# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1.split()+s2.split()
        x=Counter(s)
        a=[i for i in x if x[i]==1]
        return a
        
        