# Last updated: 20/07/2026, 18:39:31
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        stack=[]
        # return " ".join(s[::-1])
        for i in range(len(s)-1,-1,-1):
            stack.append(s[i])
        return " ".join(stack)
