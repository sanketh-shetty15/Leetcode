# Last updated: 20/07/2026, 18:38:34
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        return s in (s+s)[1:-1]
