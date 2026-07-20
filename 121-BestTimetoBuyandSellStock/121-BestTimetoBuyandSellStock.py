# Last updated: 20/07/2026, 19:39:02
1
2class Solution:
3    def maxProfit(self, prices: List[int]) -> int:
4        minimum = prices[0]
5        profit = 0
6
7        for i in range(1, len(prices)):
8            if prices[i] < minimum:
9                minimum = prices[i]
10            else:
11                profit = max(profit, prices[i] - minimum)
12
13        return profit
14
15
16
17
18        