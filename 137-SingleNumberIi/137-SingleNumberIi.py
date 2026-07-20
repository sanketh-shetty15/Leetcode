# Last updated: 20/07/2026, 18:39:39
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
             if not nums.count(i)==3:
                stack.append(i)
        return stack[0]


        