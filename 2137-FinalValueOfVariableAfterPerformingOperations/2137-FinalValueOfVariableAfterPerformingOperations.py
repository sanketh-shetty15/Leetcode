# Last updated: 20/07/2026, 18:37:34
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if (i=='--X') or (i=='X--'):
                x-=1
            else:
                x+=1
        return x
        