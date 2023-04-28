# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s1=[]
        for i in s.split():
            if i.isdigit():
                s1.append(int(i))
        if s1==sorted(set(s1)):
            return True
        else:
            return False