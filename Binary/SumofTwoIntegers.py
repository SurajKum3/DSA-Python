#  -> I used bitwise operations where XOR (^) computes the sum without carry, and AND (&) followed by a left shift computes the carry, repeat until no carry remains. Handle negative numbers by simulating 32-bit integer limits.

#  -> Time Complexity : O(1) - The loop runs for a fixed number of iterations (at most 32 bits), regardless of input size.

#  -> Space Complexity : O(1) - Only a constant amount of extra space is used for variables and bit masking.👇

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        # if a is negative in 32-bit signed integer
        return a if a <= max_int else ~(a ^ mask)