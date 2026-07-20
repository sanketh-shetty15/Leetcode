# Last updated: 20/07/2026, 18:37:53
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        stack=[]
        for i in range(len(nums)):
            j=index[i]
            stack.insert(j,nums[i])
        return stack
            
        