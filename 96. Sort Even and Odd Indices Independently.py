# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in range(len(nums)):
            if i%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a=sorted(a)
        b=sorted(b)
        b=b[::-1]
        ln=min(len(a),len(b))
        for i in range(ln):
            c.append(a[i])
            c.append(b[i])
        if len(a)==ln:
            c+=b[ln:]
        else:
            c+=a[ln:]
        return c