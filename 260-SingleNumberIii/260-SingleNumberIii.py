# Last updated: 20/07/2026, 18:39:00
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        stack=[]
        stack1=[]
        for i in nums:
            if i not in stack:
                stack.append(i)
            else:
                stack.remove(i)
        return stack
        