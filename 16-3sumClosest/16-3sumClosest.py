# Last updated: 20/07/2026, 18:40:43
class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        best=float('inf')
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(best-target):
                    best=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return s
        return best
