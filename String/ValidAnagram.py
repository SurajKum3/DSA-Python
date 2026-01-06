#  -> HashMap Data Structure:- HashMap stores character frequencies to verify both strings match exactly.
#  -> Time Complexity : O(n) - Each character is visited once.
#  -> Space Complexity : O(1) for fixed alphabets, Otherwise O(k) for unique characters.👇

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0)+1
        for i in t:
            if i not in counter or counter[i] == 0:
                return False
            counter[i] -= 1
        return True        