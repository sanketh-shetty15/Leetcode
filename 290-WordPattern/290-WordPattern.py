# Last updated: 20/07/2026, 18:38:54
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        mapPS={}
        mapSP={}

        for i in range(len(pattern)):
            c1=pattern[i]
            c2=words[i]

            if c1 in mapPS:
                if mapPS[c1]!=c2:
                    return False
            else:
                mapPS[c1]=c2

            if c2 in mapSP:
                if mapSP[c2]!=c1:
                    return False
            else:
                mapSP[c2]=c1

        return True
        
        