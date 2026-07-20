# Last updated: 20/07/2026, 18:39:04
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count=0
        # count1=1
        # for i in t:
        #     if i in s:
        #         count=1
            
        # for i in s:
        #     if i in t:
        #         count1=1
        # if count==count1:
        #     return True
        # else:
        #     return False
        a=sorted(s)
        b=sorted(t)
        if a==b:
            return True
        else:
            return False


        