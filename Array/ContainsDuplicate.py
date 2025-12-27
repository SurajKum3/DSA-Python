# 1. Brute Force Approach (O(n^2))
#  -> Compares each element with every other element in the array to check for duplicates.
#  -> Straightforward but has a time complexity of O(n^2), making it less efficient for large arrays.

#  2. Sorting (O(n log n))
#  -> Sorts the array in ascending order and then checks for adjacent elements that are the same.
#  -> Sorting helps in bringing duplicates together, simplifying the check. 
#  -> It has a time complexity of O(n log n).

# 3. Hash Map (O(n)) 👇
#  -> It uses a hash map to store the elements as keys and their counts as values.
#  -> This approach provides more information than just the presence of duplicates and has a time complexity of O(n).
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >=1:
                return True
            seen[num] = seen.get(num,0) + 1
        return False;