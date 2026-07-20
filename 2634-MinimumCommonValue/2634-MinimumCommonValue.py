# Last updated: 20/07/2026, 18:37:24
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
            i=0
            j=0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]==nums2[j]:
                    return nums1[i]
                if nums1[i]<nums2[j]:
                    i+=1
                else:
                    j+=1
            return -1         










        # stack=[]
        # for i in nums1:
        #     if i in nums2:
        #         stack.append(i)
        # if len(stack)==0:
        #     return -1
        # stack.sort()
        # return stack[0]
        