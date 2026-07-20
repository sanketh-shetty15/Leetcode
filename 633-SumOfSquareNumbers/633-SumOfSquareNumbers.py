# Last updated: 20/07/2026, 18:38:20
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(c ** 0.5)

        for i in range(limit + 1):
            rem = c - i * i
            root = int(rem ** 0.5)

            if root * root == rem:
                return True

        return False