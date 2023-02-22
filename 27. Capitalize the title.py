class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a=title.title()
        s=""
        for i in a.split():
            if len(i)<3:
                s+=i.lower()+" "
            else:
                s+=i+" "
        return s.rstrip()
