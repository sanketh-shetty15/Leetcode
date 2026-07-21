# Last updated: 21/07/2026, 23:06:00
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[1])
4        count=0
5        end=intervals[0][1]
6        for i in range(1,len(intervals)):
7            if not intervals[i][0]>=end:
8                count+=1
9            else:
10                end=intervals[i][1]
11        return count
12        