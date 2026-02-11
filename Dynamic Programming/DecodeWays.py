#  -> Uses DP where dp[i] represents the number of ways to decode the substring up to index i. At each step, consider both single-digit and two-digit valid decodings and build the solution bottom-up.

#  -> Time Complexity : O(n) - The string is traversed once, and each index performs constant-time checks.

#  -> Space Complexity : O(n) - An auxiliary DP array of size n + 1 is used to store decoding counts.👇

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            one = int(s[i - 1])
            two = int(s[i - 2:i])

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]