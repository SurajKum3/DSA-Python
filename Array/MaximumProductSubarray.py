# 1. Kadane’s Algorithm Approach (O (n)) 👇
#  -> The approach is based on Kadane’s Algorithm, but adapted for products instead of sums.
#  -> I traverse the array from left to right to compute one maximum product (maxi1).
#  -> I also traverse from right to left to handle cases with an odd number of negative elements.
#  -> The final answer is the maximum of both traversals, ensuring negative-number cases are covered.
#  -> Time Complexity : O(n) and Space Complexity : O(1).

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 0;
        prod=1;
        n = len(nums)
        
        for i in range(0,n):
            prod*=nums[i];
            maxi=max(prod,maxi);
            if prod==0:
                prod=1;
        prod=1;
        for i in range(n-1,0,-1):
            prod*=nums[i];
            maxi=max(prod,maxi);
            if prod==0:
                prod=1;
        if n==1:
            maxi=nums[0];
        return maxi;
        