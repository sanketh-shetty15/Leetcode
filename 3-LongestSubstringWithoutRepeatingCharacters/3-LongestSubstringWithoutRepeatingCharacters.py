# Last updated: 06/08/2026, 20:22:11
1class Solution:
2    def threeSum(self,nums:List[int])->List[List[int]]:
3        nums.sort()
4        r=[]
5        for i in range(len(nums)):
6            if i>0 and nums[i]==nums[i-1]:
7                continue
8            l=i+1
9            h=len(nums)-1
10            while l<h:
11                s=nums[i]+nums[l]+nums[h]
12                if s==0:
13                    r.append([nums[i],nums[l],nums[h]])
14                    l+=1
15                    h-=1
16                    while l<h and nums[l]==nums[l-1]:
17                        l+=1
18                elif s<0:
19                    l+=1
20                else:
21                    h-=1
22        return r