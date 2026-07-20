# Last updated: 20/07/2026, 18:39:25
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for j in freq:
            if freq[j]>(len(nums)//2):
                return j
        

        