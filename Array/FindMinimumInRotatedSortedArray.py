# 1. Brute Force Approach (O(n))
#  -> Traverse the entire array and track the minimum element.
#  -> Simple and intuitive, 𝐛𝐮𝐭 𝐝𝐨𝐞𝐬 𝐧𝐨𝐭 𝐥𝐞𝐯𝐞𝐫𝐚𝐠𝐞 the fact that the array is sorted and rotated.

#  2. Optimal Approach: Binary Search (O(log n)) 👇
#  -> Uses the sorted nature of the array to eliminate half of the search space at each step.
#  -> At any index, one half of the array is always sorted:
#  -> If the left half is sorted, the minimum lies either at the leftmost element or in the right half.
#  -> Otherwise, the minimum lies in the left half.
#  -> This reduces time complexity from 𝐥𝐢𝐧𝐞𝐚𝐫 𝐭𝐨 𝐥𝐨𝐠𝐚𝐫𝐢𝐭𝐡𝐦𝐢𝐜.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low,high = 0,len(nums)-1
        ans = float('inf')
        while low<=high:
            mid = (low+high)//2;

            if nums[mid]<=nums[high]:
                ans = min(ans,nums[mid]);
                high = mid-1;

            else:
                ans = min(ans,nums[mid]);
                low = mid+1;
        return ans;