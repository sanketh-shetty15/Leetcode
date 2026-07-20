# Last updated: 20/07/2026, 18:37:42
class Solution:
    def findCenter(self,edges:List[List[int]])->int:
        a,b=edges[0]
        c,d=edges[1]

        if a==c or a==d:
            return a
        else:
            return b