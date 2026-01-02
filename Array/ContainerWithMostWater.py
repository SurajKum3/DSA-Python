# 1. Two Pointer Approach (O (n)) 👇
#  -> Using two pointers (left & right) avoids checking all pairs, by always moving the pointer with the smaller height, I safely discard non-optimal containers while preserving the chance of a larger area.
#  -> Time Complexity: O(n) — Each pointer moves at most once across the array, so the loop runs linearly.
#  -> Space Complexity: O(1) — Only a few variables are used, no extra data structures are required.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0;
        left = 0;
        right = len(height)-1;
        
        while left < right:
            width = right - left;
            height1 = min(height[left],height[right]);
            maxArea = max(maxArea, width * height1);

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxArea