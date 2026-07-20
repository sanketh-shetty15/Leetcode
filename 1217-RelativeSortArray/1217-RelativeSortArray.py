# Last updated: 20/07/2026, 18:37:58
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq={}
        stack=[]
        stack1=[]
        for i in arr1:
            freq[i]=freq.get(i,0)+1
        for j in arr2:
            while freq[j]>0:
                stack.append(j)
                freq[j]-=1
        for k in arr1:
            if k not in arr2:
                stack1.append(k)
        stack1.sort()
        return stack+stack1
            



        