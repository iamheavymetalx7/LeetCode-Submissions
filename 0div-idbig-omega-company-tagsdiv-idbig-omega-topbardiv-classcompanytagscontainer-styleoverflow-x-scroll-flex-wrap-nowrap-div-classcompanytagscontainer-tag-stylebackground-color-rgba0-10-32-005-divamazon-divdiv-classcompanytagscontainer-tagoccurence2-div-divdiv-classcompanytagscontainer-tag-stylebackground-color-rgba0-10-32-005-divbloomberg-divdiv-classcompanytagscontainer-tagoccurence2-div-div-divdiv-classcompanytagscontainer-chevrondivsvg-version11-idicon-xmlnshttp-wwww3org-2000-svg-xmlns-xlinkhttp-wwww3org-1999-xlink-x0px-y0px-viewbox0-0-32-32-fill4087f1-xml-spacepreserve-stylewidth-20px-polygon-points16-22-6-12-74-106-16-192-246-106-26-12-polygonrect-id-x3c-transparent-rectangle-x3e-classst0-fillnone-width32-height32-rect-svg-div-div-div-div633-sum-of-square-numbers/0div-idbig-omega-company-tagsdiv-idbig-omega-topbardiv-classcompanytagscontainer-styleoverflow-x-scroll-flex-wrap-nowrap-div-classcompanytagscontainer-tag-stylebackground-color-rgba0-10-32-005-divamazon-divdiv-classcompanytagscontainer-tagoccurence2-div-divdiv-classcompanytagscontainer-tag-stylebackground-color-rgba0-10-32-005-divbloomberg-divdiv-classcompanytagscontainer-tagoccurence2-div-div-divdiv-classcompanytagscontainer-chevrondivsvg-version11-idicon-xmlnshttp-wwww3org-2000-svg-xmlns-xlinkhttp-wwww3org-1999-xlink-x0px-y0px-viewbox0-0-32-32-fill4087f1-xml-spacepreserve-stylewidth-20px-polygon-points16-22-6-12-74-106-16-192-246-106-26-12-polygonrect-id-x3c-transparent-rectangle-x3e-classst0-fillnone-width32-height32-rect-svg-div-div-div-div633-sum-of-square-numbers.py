def isPerfectSquare(num):

    l=-1
    r = int(1e10)

    while r-l>1:
        m =(l+r)//2
        if m**2 >num:
            r=m
        else:
            l=m

    if l**2 == num:
        return True

    return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        for i in range(0,int(math.sqrt(c))+1):
            if isPerfectSquare(c-i**2):
                return True
        return False