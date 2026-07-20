# Last updated: 20/07/2026, 18:39:49
class Solution:
    def numTrees(self, n: int) -> int:
        return math.comb(2*n,n)//(n+1)


        