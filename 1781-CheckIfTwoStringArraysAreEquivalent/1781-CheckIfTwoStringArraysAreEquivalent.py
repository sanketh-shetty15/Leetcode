# Last updated: 20/07/2026, 18:37:46
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a=""
        b=""
        for i in word1:
            a=a+i
        for j in word2:
            b=b+j
        if a==b:
            return True
        else:
            return False
        

        