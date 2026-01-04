# -> Using only the modulus (%) and division (/) operators, the palindrome check works by reversing the number digit-by-digit and comparing it with the original value - no strings or extra data structures are needed, which keeps the logic clean and mathematical.

# -> Time Complexity : O(log n) — The algorithm processes each digit once, and the number of digits in an integer n is proportional to log₁₀ n.

# -> Space Complexity : O(1) — Only a few integer variables are used regardless of input size, so the solution runs in constant extra space.👇

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0;
        num = x;
        while num>0:
            n = num % 10
            rev = rev*10+n
            num = num // 10
        if x==rev:
            return True;
        return False