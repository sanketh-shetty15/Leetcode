# Last updated: 20/07/2026, 18:38:37
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1=int(num1)
        # num2=int(num2)
        # s=num1+num2
        # return str(s)

       
        sys.set_int_max_str_digits(10000)
        return str(int(num1)+int(num2))

        