# Last updated: 20/07/2026, 18:37:27
class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in s:
            if i!='*':
                a.append(i)
            elif i=='*':
                a.pop()
        return ''.join(a)
        