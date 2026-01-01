# 1. Optimized Approach (O (n)) 👇
#  -> By storing prefix products directly in the result array and integrating suffix products in a subsequent pass, the approach delivers optimal performance while adhering to interview-standard space constraints.
#  -> Time Complexity: O(n) — As it performs two linear passes over the array - one for prefix product computation and one for suffix product application.
#  -> Space Complexity: O(1) — Excluding the output array, by leveraging only two scalar variables (prefix and suffix) instead of additional data structures.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result