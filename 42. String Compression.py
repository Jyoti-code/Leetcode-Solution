class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        for i,j in itertools.groupby(chars):
            c=len(list(j))
            s.append(i)
            if c>1:
                s.extend(list(str(c)))
        chars[:]=s