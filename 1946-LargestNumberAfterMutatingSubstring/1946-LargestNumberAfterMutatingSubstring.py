# Last updated: 22/07/2026, 22:19:18
1class Solution:
2    def maximumNumber(self, num: str, change: List[int]) -> str:
3        new=""
4        start=False
5        for i in range(len(num)):
6
7                a=change[int(num[i])]
8                if start==False:
9                    if a>int(num[i]):
10                        start=True
11                        new=new+str(a)
12                    else:
13                        new=new+num[i]
14                else:
15                    if a>=int(num[i]):
16                        new=new+str(a)
17                    else:
18                        new=new+num[i:]
19                        break
20                    
21                
22        return new
23
24        