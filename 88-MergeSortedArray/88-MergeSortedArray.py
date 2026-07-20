# Last updated: 20/07/2026, 18:39:53
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted(nums1[:m]+nums2[:n])
        