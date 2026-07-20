# Last updated: 20/07/2026, 18:40:23
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:return 0
        sign=1
        if (dividend<0)^(divisor<0):sign=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=0
        while dividend>=divisor:
            temp=divisor
            multiple=1
            while dividend>=(temp<<1):
                temp<<=1
                multiple<<=1
            dividend-=temp
            res+=multiple
        res=res*sign
        return min(max(-(1<<31),res),(1<<31)-1)
