#  -> Used an iterative dynamic programming approach with space optimization, where only the last two computed results are stored to build the solution for the current step (similar to Fibonacci).

#  -> Time Complexity : O(n) - The loop runs once from step 3 to n, doing constant work in each iteration.

#  -> Space Complexity : O(1) - Only a fixed number of variables (prev1, prev2, cur) are used, no extra array or recursion stack.👇

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        
        return cur