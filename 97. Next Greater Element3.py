# https://leetcode.com/problems/next-greater-element-iii/description/

from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # pass 38 test cases
        # s=permutations(str(n))
        # a=[]
        # for i in list(s):
        #     a.append(''.join(i))
        # d=sorted(set([int(i) for i in a]))
        # x=d.index(n)
        # try:
        #     return d[x+1] if d[x+1]<=2**31-1 else -1
        # except:
        #     return -1
        # pass all
        all_nums_of_same_digits = [int(''.join(i)) for i in set(permutations(str(n)))]
        all_nums_of_same_digits.sort()
        i = all_nums_of_same_digits.index(n)
        try:
            return all_nums_of_same_digits[i + 1] if all_nums_of_same_digits[i + 1] <= 2**31-1    else -1
        except:
            return -1
