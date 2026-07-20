# Last updated: 20/07/2026, 18:39:02
class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            num = total

        return num

        