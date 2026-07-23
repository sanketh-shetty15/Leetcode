# Last updated: 23/07/2026, 16:49:49
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5
6        tank = start = 0
7
8        for i in range(len(gas)):
9            tank += gas[i] - cost[i]
10
11            if tank < 0:
12                tank = 0
13                start = i + 1
14
15        return start
16        