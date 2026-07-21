# Last updated: 21/07/2026, 20:17:04
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest=-1
        a=""
        for i in range(1,len(num)-1):
            if num[i-1]==num[i]==num[i+1]:
                largest=max(largest,int(num[i]))
        if largest==-1:
            return ""
        else:
             return str(largest)*3



        
        