#  -> Started from the last index and move backward, updating the goal whenever the current index can reach it. If I can finally move the goal to index 0, the jump is possible.

#  -> Time Complexity : O(n) - The array is traversed exactly once from right to left, making it linear time.

#  -> Space Complexity : O(1) - Only a single variable (goal) is used, no extra data structures are required.👇

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False