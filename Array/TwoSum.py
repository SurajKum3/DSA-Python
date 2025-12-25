# 1. Brute Force Approach
# Check every pair of elements to see if their sum equals the target.

# Time Complexity: O(n²)

# Space Complexity: O(1)

# Simple but inefficient for large inputs.

# 2. HashMap Approach (Better Solution)
# Store each element in a hash map and check if its complement (target - element) exists.

# Time Complexity: O(n)

# Space Complexity: O(n)

# Fastest and most commonly used solution.

# 3. Sorting + Two Pointer Approach (Optimal Pattern)
# Sort the array (while keeping original indices) and use two pointers to find the target sum.

# Time Complexity: O(n log n)

# Space Complexity: O(n)

# Useful when two-pointer technique or sorted array is required.

# 👉 Best Overall: HashMap approach
# 👉 Best without HashMap: Sorting + Two Pointers


# Sorting + Two Pointer Approach (Optimal Pattern) 👇
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = [(num, i) for i, num in enumerate(nums)]
        final.sort(key=lambda x: x[0])
        
        low,high = 0,len(nums)-1
        
        while low<high:
            numbers = final[low][0] + final[high][0]
            if (numbers == target):
                return [final[low][1],final[high][1]]
            elif(numbers>target):
                high -= 1
            else:
                low += 1