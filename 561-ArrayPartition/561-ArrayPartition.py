# Last updated: 20/07/2026, 18:38:24
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(0,len(nums),2):
            total=total+nums[i]
        return total
        