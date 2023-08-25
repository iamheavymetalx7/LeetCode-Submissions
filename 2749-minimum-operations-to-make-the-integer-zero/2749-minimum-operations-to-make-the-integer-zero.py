'''
https://www.youtube.com/watch?v=7RNDbY1Qaig
'''
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(60):
            val = num1-num2*i
            set_bits = val.bit_count()
            
            if val>=0 and set_bits<=i<=val:
                return i
        return -1
        