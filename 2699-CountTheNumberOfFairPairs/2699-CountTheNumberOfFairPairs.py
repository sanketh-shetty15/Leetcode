# Last updated: 20/07/2026, 18:37:21
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         count=0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if lower<=nums[i]+nums[j]<=upper:
#                     count+=1
#         return count
        

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() 
        res = 0

        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            res += right - left

        return res