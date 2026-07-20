# Last updated: 20/07/2026, 18:40:20
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2;
            if nums[mid]==target:
                return mid;
            elif nums[mid]<target:
                low=mid+1;
            else:
                high=mid-1;
        return low;
        