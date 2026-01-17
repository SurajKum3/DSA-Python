#  -> The solution iteratively processes all 32 bits, extracting the least significant bit of n, appending it to result using a left shift and bitwise OR, and then right shifting n to move to the next bit.

#  -> Time Complexity : O(1) - The loop always runs for a fixed 32 iterations, independent of the input value.

#  -> Space Complexity : O(1) - Only a constant amount of extra space is used (result and loop variables), with no additional data structures.👇

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result