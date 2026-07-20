# Last updated: 20/07/2026, 18:38:55
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack=[]
        stack1=[]
        for i in nums:
            if i!=0:
                stack.append(i)
            else:
                stack1.append(i)
        nums[:]=stack+stack1
        