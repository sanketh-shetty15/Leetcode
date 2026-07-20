# Last updated: 20/07/2026, 18:37:32
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0
        freq={}
        freq1={}
        for i in words1:
            if words1.count(i)==1 and i in words2:
                if words2.count(i)==1:
                    count+=1
        return count
        # for i in words1:
        #     freq[i]=freq.get(i,0)+1
        # for j in words2:
        #     freq1[j]=freq1.get(j,0)+1
        # for k in words1:
        #     if k in words2:
        #         if freq[k]==1 and freq1[k]==1:
        #             count+=1
        # return count

        
        