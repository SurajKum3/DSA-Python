#  -> Applied the sliding window technique with two pointers and a hash map to maintain a window of unique characters, shrinking the window immediately when a duplicate is detected.
#  -> Time Complexity : O(n) - Because each character is visited at most twice - once by the right pointer and once by the left pointer.
#  -> Space Complexity : O(min(n,k)) - Where k is the size of the character set, since the hash map stores only unique characters within the current window.👇

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = left = 0
        count = {}

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right - left + 1)

        return max_length