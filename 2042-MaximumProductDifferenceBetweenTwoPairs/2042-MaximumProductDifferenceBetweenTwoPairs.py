# Last updated: 20/07/2026, 18:37:38
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        b=nums[0]
        c=nums[1]
        d=nums[-1]
        e=nums[-2]
        result=(e*d)-(b*c)
        return result