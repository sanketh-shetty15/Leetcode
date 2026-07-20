# Last updated: 20/07/2026, 18:37:14
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        m=str(n)
        freq={}
        total=0
        for i in m:
            freq[i]=freq.get(i,0)+1
        
        for i in freq:
            total=total+int(i)*freq[i]
        return total

            

        