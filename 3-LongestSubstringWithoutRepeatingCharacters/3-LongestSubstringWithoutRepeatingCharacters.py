# Last updated: 20/07/2026, 20:41:47
1# class Solution:
2#     def lengthOfLongestSubstring(self, s: str) -> int:
3#         stack=[]
4#         total=0
5#         max_sum=0
6#         if s=="":
7#             return 0
8#         elif s==" ":
9#             return 1
10#         else:
11#             for i in range(len(s)):
12#                 if s[i] not in stack:
13#                     stack.append(s[i])
14#                 else:
15#                     total=len(stack)
16#                     max_sum=max(max_sum,total)
17#                     stack.clear()
18#                     stack.append(s[i])
19#             return max_sum
20        # b=set(s)
21
22class Solution:
23    def lengthOfLongestSubstring(self, s: str) -> int:
24        stack = []
25        max_len = 0
26
27        for ch in s:
28            while ch in stack:
29                stack.pop(0)      
30
31            stack.append(ch)      
32            max_len = max(max_len, len(stack))
33
34        return max_len
35        