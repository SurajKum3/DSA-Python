#  -> The solution leverages Python’s list multiplication (nums * 2) to concatenate the array with itself in a single, concise operation instead of using loops.

#  -> Time Complexity : O(n) - Each element is copied twice to form the new list.

#  -> Space Complexity : O(n) - Additional space is required to store the concatenated array of size 2n.👇

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2