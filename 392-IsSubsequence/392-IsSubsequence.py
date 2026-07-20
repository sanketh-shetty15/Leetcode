# Last updated: 20/07/2026, 18:38:40
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for ch in t:
            if i<len(s) and ch==s[i]:
                i+=1

        return i==len(s)

        
        