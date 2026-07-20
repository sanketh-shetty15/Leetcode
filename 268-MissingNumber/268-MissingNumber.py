# Last updated: 20/07/2026, 18:38:57
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n =len(nums)
        # Tsum=(n*(n+1)) //2
        # Asum=sum(nums)
        # return Tsum - Asum
        a=[]
        b=sorted(nums)
        start=min(b)
        end=len(b)
        
        for i in range(0,end+1):
            a.append(i)
        for j in a:
            if j not in nums:
                return j
        if len(nums)==1:
            return 0

