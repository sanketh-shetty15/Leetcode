# Last updated: 20/07/2026, 20:09:36
1class Solution:
2    def largestGoodInteger(self, num: str) -> str:
3        largest=-1
4        a=""
5        for i in range(1,len(num)-1):
6            if num[i-1]==num[i]==num[i+1]:
7                largest=max(largest,int(num[i]))
8        if largest==-1:
9            return ""
10        else:
11             return str(largest)*3
12
13
14
15        
16        