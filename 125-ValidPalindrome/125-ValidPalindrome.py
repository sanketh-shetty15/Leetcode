# Last updated: 20/07/2026, 18:39:44
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in s:
            if i.isalnum():
                new=new+i.lower()
        return new==new[::-1]  


