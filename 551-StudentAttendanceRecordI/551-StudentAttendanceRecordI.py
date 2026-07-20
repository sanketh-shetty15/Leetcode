# Last updated: 20/07/2026, 18:38:25
class Solution:
    def checkRecord(self, s: str) -> bool:
        a=s.count("A")
        if a>=2:
            return False
        else:
            for i in range(len(s)-2):
                if s[i]=="L" and s[i+1]=="L" and s[i+2]=="L":
                    return False
            
        return True
        