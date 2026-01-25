#  -> Use two pointers starting from the end of both arrays and fill nums1 from the back to avoid overwriting existing elements, always placing the larger value at the current rightmost position.

#  -> Time Complexity : O(m+n) - Each element from nums1 and nums2 is visited and placed exactly once.

#  -> Space Complexity : O(1) - The merge is done in-place using only constant extra variables, with no additional data structures.👇

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1