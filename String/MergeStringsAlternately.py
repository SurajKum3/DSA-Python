#  -> Used simultaneous traversal with zip() to merge characters alternately, then appended the remaining substring of the longer string to handle unequal lengths cleanly.

#  -> Time Complexity : O(n+m) - Where n and m are the lengths of word1 and word2, each character is processed exactly once.

#  -> Space Complexity : O(n+m) - Due to the auxiliary list merged used to store intermediate results before joining into the final string.👇

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)