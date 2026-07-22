# Last updated: 22/07/2026, 19:37:14
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        minimum=prices[0]
4        profit=0
5        total=0
6        for i in range(1,len(prices)):
7            if prices[i]<minimum:
8                minimum=prices[i]
9            else:
10                profit=prices[i]-minimum
11                total=total+profit
12                minimum=prices[i]
13        return total
14        