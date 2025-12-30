# - Key Learnings / Takeaways:
#  -> Time Complexity : O(n)
#  -> Space Complexity : O(1)
#  -> Maintain a variable 'minimum' to store the lowest stock price encountered up to the current day.
#  -> For every day, compute profit as 'prices[i] - minimum', assuming you sell on that day.
#  -> Keep updating 'maxProfit' with the maximum profit obtained so far.
#  -> Since 'minimum' is updated before future days, the algorithm naturally ensures buying happens before selling.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0];
        maxProfit = 0;
        n = len(prices);
        for i in range(0,n):
            cost = prices[i] - mini;
            maxProfit = max(maxProfit, cost);
            mini = min(mini,prices[i]);
        return maxProfit;