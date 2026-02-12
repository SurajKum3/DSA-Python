#  -> Approach (DP – Space Optimized)
#  - For each house, choose: rob it (prev_rob + cur_val) or skip it (max_rob).
#  - Uses two variables to simulate dp[i-1] and dp[i-2].

#  -> Time Complexity : O(n) - Single pass through the array → linear time.

#  -> Space Complexity : O(1) - Only two variables used → constant extra space.👇

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = max_rob = 0

        for cur_val in nums:
            temp = max(max_rob, prev_rob + cur_val)
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob