#  -> Use Dynamic Programming where dp[i] indicates whether the substring s[:i] can be segmented using words from wordDict. For each position i, check all words and mark dp[i] = True if a valid split exists.

#  -> Time Complexity : O(n * m * k) - O(n × m × k), where n is the length of the string s, m is the number of words in wordDict, and k is the average length of a word (due to substring comparison).

#  -> Space Complexity : O(n) - O(n) for the DP array of size len(s) + 1, used to store segmentation validity.👇

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]