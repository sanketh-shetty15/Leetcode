# Last updated: 20/07/2026, 18:40:26
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack=[]
        for i in nums:
            if i!=val:
                stack.append(i)
        nums[:len(stack)]=stack
        return len(stack)

        