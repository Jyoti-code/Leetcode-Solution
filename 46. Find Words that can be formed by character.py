class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        a=0
        for i in words:
            for j in i:
                if i.count(j)>chars.count(j):
                    break
            else:
                a+=len(i)
        return a