#  -> I used bitwise operations where XOR (^) computes the sum without carry, and AND (&) followed by a left shift computes the carry, repeat until no carry remains. Handle negative numbers by simulating 32-bit integer limits.

#  -> Time Complexity : O(1) - The loop runs for a fixed number of iterations (at most 32 bits), regardless of input size.

#  -> Space Complexity : O(1) - Only a constant amount of extra space is used for variables and bit masking.👇

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res