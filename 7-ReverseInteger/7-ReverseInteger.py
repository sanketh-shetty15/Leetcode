# Last updated: 20/07/2026, 18:40:58
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=str(-x)
            rev=-int(x[::-1])
        else:
            x=str(x)
            rev=int(x[::-1])
        if rev<-2**31 or rev>2**31-1:
            return 0

        return rev        

        