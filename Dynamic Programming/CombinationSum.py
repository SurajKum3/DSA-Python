#  -> Uses backtracking to explore all possible combinations by either including the current element (without moving index) or excluding it (moving to the next index), ensuring all valid combinations that sum to the target are generated.

#  -> Time Complexity : O(2^n) - The time complexity is exponential, approximately O(2^N) in the worst case, since each element has two choices (pick or not pick) and all possible combinations are explored.

#  -> Space Complexity : O(t/d) - Where t is the target and d is the smallest candidate, representing the depth of the recursion.👇

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res

        return make_combination(0, [], 0)