# Last updated: 20/07/2026, 18:40:27
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
            if i not in stack:
                stack.append(i)
        for i in range(len(stack)):
            nums[i] = stack[i]

        return len(stack)
