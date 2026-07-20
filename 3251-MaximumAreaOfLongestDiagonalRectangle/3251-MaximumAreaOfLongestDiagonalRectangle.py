# Last updated: 20/07/2026, 18:37:16
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        a=0
        b=0
        for l,w in dimensions:
            store=sqrt(((l*l)+(w*w)))
            if store>a  or (store==a and l*w>b):
                a=store
                b=l*w
        return b
            
                

        