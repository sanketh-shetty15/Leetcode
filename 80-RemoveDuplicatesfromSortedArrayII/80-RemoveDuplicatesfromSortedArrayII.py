# Last updated: 01/08/2026, 18:04:26
1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack=[]
4        for i in range(len(nums1)):
5            if nums1[i] in nums2:
6                    stack.append(nums1[i])
7                    nums2.remove(nums1[i])
8        return stack
9        