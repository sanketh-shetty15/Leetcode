# Last updated: 20/07/2026, 18:40:08
class Solution:
    def canJump(self, nums):
        reach = 0
        for i, jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + jump)
        return True
