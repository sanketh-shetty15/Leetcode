# Last updated: 20/07/2026, 18:38:32
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack=[]
        count=0
        for i in nums:
            if i==1:
                count+=1
            elif i==0:
                 stack.append(count)
                 count=0
        stack.append(count)
            
        a=max(stack)
        return a

