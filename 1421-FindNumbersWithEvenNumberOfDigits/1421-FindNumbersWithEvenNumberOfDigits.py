# Last updated: 20/07/2026, 18:37:55
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            i=str(i)
            a=len(i)
            if a%2==0:
                count+=1
        return count
        