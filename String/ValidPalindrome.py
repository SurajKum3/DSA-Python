#  -> Clean the string by keeping only lowercase alphanumeric characters, then use two pointers (left and right) starting from both ends to compare characters and move inward until they meet or a mismatch is found.

#  -> Time Complexity : O(n) - Each character is processed at most once during string cleaning and once during the two-pointer comparison.

#  -> Space Complexity : O(n) - Extra space is used to store the filtered and normalized string.👇

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True