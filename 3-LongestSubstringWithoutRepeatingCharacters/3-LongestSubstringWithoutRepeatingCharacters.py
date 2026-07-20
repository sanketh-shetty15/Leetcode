# Last updated: 20/07/2026, 18:41:02
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
            else:
                while stack and stack[0] != s[i]:
                    stack.pop(0)
                stack.pop(0)
                stack.append(s[i])

            if len(stack) > count:
                count = len(stack)

        return count
