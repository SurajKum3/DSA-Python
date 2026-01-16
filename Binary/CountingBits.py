#  -> Uses Dynamic Programming by tracking the most recent power of 2 (sub). For each number i, the number of set bits is computed as dp[i - sub] + 1, leveraging previously computed results.

#  -> Time Complexity : O(n) - The loop runs once from 1 to n, and each operation inside the loop is constant time.

#  -> Space Complexity : O(n) - An extra array dp of size n + 1 is used to store the count of set bits for each number.👇

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp