# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]