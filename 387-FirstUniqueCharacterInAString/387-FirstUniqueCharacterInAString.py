# Last updated: 20/07/2026, 18:38:43
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in s:
#             if s.count(i)==1:
#                 return s.index(i)
            
#         return -1

class Solution():
    def firstUniqChar(self, s):
        a = collections.Counter(s);
        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1       
            

                
        