#  -> Uses two pointers from both ends of the string. On the first mismatch, try skipping either the left or right character and check if the remaining substring is a palindrome, allowing at most one deletion.

#  -> Time Complexity : O(n) - Each character is visited at most a constant number of times. Even with the extra palindrome checks, the total work remains linear.

#  -> Space Complexity : O(1) - The solution uses constant extra space since all checks are done using pointers without additional data structures.👇

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True