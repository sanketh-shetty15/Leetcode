# Last updated: 20/07/2026, 18:37:28
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        stack=[]

        freq={}
        for i in nums:
            freq[i]=freq.get(i, 0)+1

        for i in nums:
            a=freq[i]
            if not (a>1 or (i-1) in freq or (i+1) in freq):
                stack.append(i)

        return stack