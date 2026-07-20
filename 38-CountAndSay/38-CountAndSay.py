# Last updated: 20/07/2026, 18:40:16
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(n - 1):
            result = self.build(result)
        
        return result

    def build(self, s: str) -> str:
        """Helper to read off the digits and build next term."""
        output = ""
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                output += str(count) + s[i - 1]
                count = 1
        
        output += str(count) + s[-1]
        
        return output
