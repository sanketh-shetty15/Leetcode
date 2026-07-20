# Last updated: 20/07/2026, 18:39:42
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
            if i not in stack:
                stack.append(i)
            else:
                stack.remove(i)
        return stack[0]
        