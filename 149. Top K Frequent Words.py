# https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words=sorted(words)
        x=Counter(words)
        a=[i for i,j in x.most_common(k)]
        return a