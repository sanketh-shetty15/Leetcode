# Last updated: 20/07/2026, 18:38:27
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)   
        
        for i in range(0,len(s),2*k):
            s[i:i+k]=reversed(s[i:i+k])
        return "".join(s)
