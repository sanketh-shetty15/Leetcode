# Last updated: 20/07/2026, 18:40:24
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        n=len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
        
        