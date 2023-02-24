class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c * t for c, t in collections.Counter(s).most_common())