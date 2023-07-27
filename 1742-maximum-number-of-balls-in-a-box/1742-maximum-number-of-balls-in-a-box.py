class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        
        boxes=[0]*(highLimit+1)
        
        
        def calcsum(x):
            xx = str(x)
            summ=0
            for e in xx:
                summ+=int(e)
            return summ
        
        
        for i in range(lowLimit, highLimit+1):
            val = calcsum(i)
            boxes[val]+=1
        
        return max(boxes)
        