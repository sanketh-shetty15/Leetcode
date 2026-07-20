# Last updated: 20/07/2026, 18:38:42
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        for i in t:
            if i in s:
                s.remove(i)
            else:
                return i

                
                
            

        