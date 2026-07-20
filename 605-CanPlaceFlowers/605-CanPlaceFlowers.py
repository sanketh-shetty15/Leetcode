# Last updated: 20/07/2026, 18:38:22
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if len(flowerbed) == 1:
            if n == 0:
                return True
            if flowerbed[0] == 0 and n <= 1:
                return True
            return False


        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            c=c+1

        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c=c+1
       
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            c=c+1
            
        if c>=n:
            return True
        else:
            return False

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         c = 0
        
#         if flowerbed[0] == 0 and flowerbed[1] == 0:
#             flowerbed[0] = 1
#             c += 1
        
#         for i in range(1, len(flowerbed)-1):
#             if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                 flowerbed[i] = 1
#                 c += 1
        
#         if flowerbed[-1] == 0 and flowerbed[-2] == 0:
#             flowerbed[-1] = 1
#             c += 1
            
#         if c >= n:
#             return True
#         else:
#             return False
        