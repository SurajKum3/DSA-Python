# 1. Linear Search Approach (O(n))
#  -> Traverse the array element by element until the target is found or the array ends.
#  -> Time Complexity : O(n) - In the worst case, every element must be checked.

# 2. Binary Search Approach (O(log n)) 👇
#  -> Use modified binary search by identifying the sorted half of the rotated array at each step.
#  -> Time Complexity: O(log n) - The search space is halved at every step.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1;
        while(low<=high):
            mid = int((low+high) / 2)

            if (nums[mid]==target):
                return mid;
            
            if (nums[low] <= nums[mid]):
                if(nums[low] <= target and target <= nums[mid]):
                    high = mid - 1;
                else:
                    low = mid + 1;
            else:
                if(nums[mid]<=target and target<=nums[high]):
                    low = mid+1;
                else:
                    high = mid-1;
        return -1;