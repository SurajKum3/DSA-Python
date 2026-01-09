#  -> I used the expand around center technique for each index to count both odd (i, i) and even (i, i+1) length palindromes.
#  -> Time Complexity : O(n^2) - Each expansion can take O(n) and is done for n indices, resulting in O(n²) time complexity.
#  -> Space Complexity : O(1) - Only constant extra variables are used, so the space complexity is O(1).👇

class Solution:
    def countSubstrings(self, s: str) -> int:        
        res = 0

        def count_palindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count

        for i in range(len(s)):
            res += count_palindrome(s, i, i)
            res += count_palindrome(s, i, i + 1)
        
        return res