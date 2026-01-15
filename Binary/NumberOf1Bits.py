#  -> I iterate through all 32 bit positions of the integer, right-shift the number by i, check the least significant bit using & 1, and increment the count whenever the bit is set.

#  -> Time Complexity : O(1) - The loop always runs for a fixed 32 iterations regardless of input size.

#  -> Space Complexity : O(1) - Only a constant variable (res) is used, with no extra memory proportional to input size.👇

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res