#  -> Used a two-pointer technique where one pointer (i) scans the array and another (index) tracks the position to place elements not equal to val, effectively overwriting unwanted elements in-place.

#  -> Time Complexity : O(n) - The array is traversed exactly once, where n is the length of nums.

#  -> Space Complexity : O(1) - No extra space is used apart from a few variables; the operation is done in-place.👇

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index