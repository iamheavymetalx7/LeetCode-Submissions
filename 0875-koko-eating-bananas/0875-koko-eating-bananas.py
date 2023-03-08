class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(m,piles):
            cnt = 0
            for i in range(len(piles)):
                cnt += int(math.ceil(piles[i]/m))
            # print(cnt,"inside canEat")
            if cnt<=h:
                return True
            return False
                
        
        l,r = 0,int(1e18)

        while r>l+1:
            # print(l,r,"left, right")
            m = (l+r)//2
            # print(m,"middle val")
            
            if canEat(m,piles):
                r=m
            else:
                l=m
        # print("done here................")
        return r