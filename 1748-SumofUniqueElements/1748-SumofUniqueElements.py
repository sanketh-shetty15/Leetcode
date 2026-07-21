# Last updated: 21/07/2026, 20:15:29
1class Solution:
2    def sumOfUnique(self, nums: List[int]) -> int:
3        total=0
4        for i in nums:
5            if nums.count(i)==1:
6                total=total+i
7        return total
8
9        