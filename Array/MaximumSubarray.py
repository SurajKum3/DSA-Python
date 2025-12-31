# 1. Brute Force Approach (Three Loops: i, j, k)
#  -> Try all possible subarrays using three nested loops and calculate the sum of each subarray.
#  -> Time Complexity: O(n³) — i loop for start, j loop for end, k loop to calculate sum.
#  -> Space Complexity: O(1) — No extra space used apart from variables.

#  2. Improved Brute Force Approach (Two Loops: i, j)
#  -> Fix the starting index i, keep adding elements using sum += arr[j], and compare with maximum.
#  -> Time Complexity: O(n²) — i loop for start, j loop for extending the subarray.
#  -> Space Complexity: O(1) — Uses only constant extra variables.

#  3. Kadane’s Algorithm (Optimal Approach) 👇
#  -> Keep track of the maximum subarray ending at each index and reset sum when it becomes negative.
#  -> Time Complexity: O(n) — Single traversal of the array.
#  -> Space Complexity: O(1) — No additional data structures used.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0;
        maxi = nums[0];
        n = len(nums);
        for i  in range(0,n):
            sum += nums[i];
            if sum > maxi:
                maxi = sum;
            if sum<0:
                sum = 0;
        return maxi