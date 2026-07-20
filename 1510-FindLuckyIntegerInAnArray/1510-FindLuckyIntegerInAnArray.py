# Last updated: 20/07/2026, 18:37:52
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        ans=-1
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for j in freq:
            if j==freq[j]:
                ans=max(ans,j)
        return ans
            


        