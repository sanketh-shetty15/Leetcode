# Last updated: 03/08/2026, 19:27:37
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        stack = []
4        i = 0
5        j = 0
6
7        while i < len(word1) and j < len(word2):
8            stack.append(word1[i])
9            stack.append(word2[j])
10            i += 1
11            j += 1
12
13        while i < len(word1):
14            stack.append(word1[i])
15            i += 1
16
17        while j < len(word2):
18            stack.append(word2[j])
19            j += 1
20
21        return "".join(stack)