# Last updated: 20/07/2026, 18:40:05
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in range(len(s)-1,-1,-1):
            if count!=0 and s[i]==" ":
                break
            elif s[i]==" ":
                continue
            else:
                count+=1
            
        return count
        


        