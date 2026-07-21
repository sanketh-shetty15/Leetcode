# Last updated: 21/07/2026, 20:17:14
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            if nums.count(i)==1:
                total=total+i
        return total

        