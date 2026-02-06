#  -> Used a greedy + binary search (patience sorting) strategy where res maintains the smallest possible tail for increasing subsequences of different lengths, binary search helps replace elements efficiently without breaking order.

#  -> Time Complexity : O(nlogn) - Each of the n elements is processed once, and binary search on res takes O(log n) in the worst case.

#  -> Space Complexity : O(n) - Extra space is used for the res array which can grow up to the length of the input in the strictly increasing case.👇

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        
        return len(res)