def sumofsquare(a):
    s = str(a)
    ans = 0
    for i in s:
        ans += (int(i))**2
    return ans



class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        
        while n not in numbers:
            numbers.add(n)
            a = sumofsquare(n)
            #print(a)
            if a ==1:
                return True
            #print(numbers)
            n = a
        return False
        
        