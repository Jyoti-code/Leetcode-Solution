# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        x=[]
        arr.sort()
        if len(arr) < 3: return []
        if arr[0] > 0: return []
        for i in range(len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                continue
            l=i+1
            r=len(arr)-1
            while l<r:
                a=arr[i]+arr[l]+arr[r]
                if a<0:
                    l+=1
                elif a>0:
                    r-=1
                else:
                    x.append([arr[i],arr[l],arr[r]])
                    while l<r and arr[l]==arr[l+1]:
                        l+=1
                    while l<r and arr[r]==arr[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return x

            
