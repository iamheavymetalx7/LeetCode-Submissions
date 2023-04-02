class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        m=len(spells)
        ans=[]
        for i,sp in enumerate(spells):
            cnt=0
            need= math.ceil(success/sp)
            
            idx= bisect.bisect_left(potions,need)
            
            if idx>=n:
                ans.append(0)
                continue
            cnt=(n)-idx
            ans.append(cnt)
        return ans
            
            
        
        
        