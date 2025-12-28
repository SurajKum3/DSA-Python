# 1. Brute Force Approach (O(n^3))
#  -> Uses three for-loops to check every possible triplet in the array.
#  -> Time Complexity : O(n³) due to three nested iterations.

#  2. Optimal Approach (Sorting + Two Pointers) (O(n^2)) 👇
#  -> Sort the array, fix one element, and use two pointers to find remaining two values.
#  -> Time Complexity: O(n²) sorting and two-pointer traversal approach.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0,n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,n-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k];
                if sum < 0:
                    j+=1;
                elif sum > 0:
                    k-=1;
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1;
                    k-=1;
                    while(j < k and nums[j] == nums[j-1]):
                        j+=1
                    while(j < k and nums[k] == nums[k+1]):
                        k-=1
        return res;