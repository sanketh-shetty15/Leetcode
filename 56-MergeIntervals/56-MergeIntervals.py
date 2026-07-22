# Last updated: 22/07/2026, 22:59:41
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        stack = []
4        intervals.sort()
5
6        if len(intervals) > 1:
7            stack.append(intervals[0])
8
9            for i in range(1, len(intervals)):
10                if stack[-1][1] >= intervals[i][0]:
11                    stack[-1][1] = max(stack[-1][1], intervals[i][1])
12                else:
13                    stack.append(intervals[i])
14        else:
15            stack = intervals
16
17        return stack