# Last updated: 20/07/2026, 18:38:45
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=0
        ransomNote=sorted(ransomNote)
        magazine=sorted(magazine)
        for i in ransomNote:
            if i in magazine:
                count=1
                magazine.remove(i)
            else:
                return False
            
        if count==1:
            return True
        

                 
        