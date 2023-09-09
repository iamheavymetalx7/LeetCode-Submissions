class Solution:
    def countBlackBlocks(self, n: int, m: int, coordinates: List[List[int]]) -> List[int]:
        
        mp = defaultdict(int)
        
        
        for x,y in coordinates:
            if x==n-1 and y==m-1:
                mp[(x-1,y-1)]+=1
            
            elif x==n-1:
                mp[(x-1,y)]+=1
                mp[(x-1,y-1)]+=1
            
            elif y==m-1:
                mp[(x,y-1)]+=1
                mp[(x-1,y-1)]+=1
            else:
                mp[(x-1,y-1)]+=1
                mp[(x-1,y)]+=1
                mp[(x,y-1)]+=1
                mp[(x,y)]+=1
            
        ans =[0]*(5)
        curr = (n-1)*(m-1)
        for (a,b),v in mp.items():
            if a>=0 and b>=0:
                ans[v]+=1
            
        ans[0]=curr
        for i in range(1,5):
            ans[0]-=ans[i]
        
        return ans
        
        
                