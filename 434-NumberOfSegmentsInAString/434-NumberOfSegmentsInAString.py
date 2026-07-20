# Last updated: 20/07/2026, 18:38:35
class Solution:
    def countSegments(self, s: str) -> int:
        count=0
        s=s.split()
        for i in s:
           count=count+1
        return count

            
        