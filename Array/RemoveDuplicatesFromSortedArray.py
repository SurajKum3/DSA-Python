#  -> Use two pointers where i tracks the position of the last unique element and j scans the array, whenever a new unique value is found, increment i and overwrite nums[i] with that value.

#  -> Time Complexity : O(n) - Each element is visited exactly once by the pointer j.

#  -> Space Complexity : O(1) - Duplicates are removed in-place, using only constant extra space.👇

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1