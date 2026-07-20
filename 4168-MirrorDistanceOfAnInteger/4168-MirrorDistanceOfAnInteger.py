# Last updated: 20/07/2026, 18:37:18
class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=str(n)
        # result=""
        a="".join(reversed(m))
        a=int(a)
        result=abs(n-a)
        return result
        # for i in range(len(m)-1,-1,-1):
        #     result=result+m[i]
        # result=int(result)
        # total=abs(n-result)
        # return total