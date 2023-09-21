class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        
        
        l=0
        r=int(1e18)
        
        def check(mid):
            blossom =[]
            for i in range(n):
                if bloomDay[i]<=mid:
                    blossom.append(True)
                else:
                    blossom.append(False)

            cnt=0
            bouquet =0
            for x in blossom:
                if x:
                    cnt+=1
                else:
                    cnt=0
                    
                if cnt==k:
                    bouquet+=1
                    cnt=0
            return bouquet>=m
        
                
                    
            
        
        while r-l>1:
            mid = (l+r)//2
            
            if check(mid):
                r=mid
            else:
                l=mid
        return r