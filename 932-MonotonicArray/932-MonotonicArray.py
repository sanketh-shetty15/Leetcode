# Last updated: 20/07/2026, 18:38:07
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        k=0
        m=0
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:  
                k=1
            elif nums[i]>nums[i+1]:
                m=1
        if k==1 and m==1:
            return False
        else:
            return True

        

        

        