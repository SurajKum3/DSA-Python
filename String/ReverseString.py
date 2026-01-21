#  -> Uses the two pointers technique, where one pointer starts from the beginning and the other from the end, swapping characters and moving inward until both pointers meet.

#  -> Time Complexity : O(n) - Each character is visited and swapped at most once, where n is the length of the string.

#  -> Space Complexity : O(1) - The string is reversed in-place without using any extra data structures.👇

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1;
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1;
            right -= 1;