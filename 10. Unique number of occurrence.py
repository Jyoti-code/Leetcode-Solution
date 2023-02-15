from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr1=Counter(arr)
        st=set()
        for i in arr1:
            st.add(arr1[i])
        if len(arr1)==len(st):
            return True
        return False
        