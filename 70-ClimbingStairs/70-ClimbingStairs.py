# Last updated: 20/07/2026, 18:39:57
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        a=3
        b=2
        for i in range(3,n):
            output=a+b
            b=a
            a=output
        return output
        