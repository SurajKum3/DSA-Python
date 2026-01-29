#  -> Maintain a window with character frequencies and track the maximum frequency in the window. If (window length − max frequency) > k, shrink the window from the left to restore validity while maximizing the window size.

#  -> Time Complexity : O(n) - Each character is added to and removed from the sliding window at most once, where n is the length of the string.

#  -> Space Complexity : O(1) - The frequency map stores at most 26 characters (uppercase English letters), which is constant space.👇

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - i + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res 