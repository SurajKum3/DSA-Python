#  -> Convert the circular problem into two linear subproblems - rob houses from 0 to n-2 and from 1 to n-1, then take the maximum of both using a space-optimized DP helper.

#  -> Time Complexity : O(n) - Each house is processed once in each of the two linear passes.

#  -> Space Complexity : O(1) - Only constant extra space is used (prev_rob and max_rob), no DP array.👇

class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            prev_rob = max_rob = 0

            for cur_val in nums:
                temp = max(max_rob, prev_rob + cur_val)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob
        
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])