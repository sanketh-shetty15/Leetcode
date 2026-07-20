# Last updated: 20/07/2026, 18:38:02
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack) 