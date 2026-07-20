# Last updated: 20/07/2026, 18:39:30
class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=nums[0]
        for i in nums:
            if i<a:
                a=i
        return a
        