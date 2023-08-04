class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        
        cnt =0
        rungs.insert(0,0)
        
        # print(rungs)
        
        
        for i in range(1,len(rungs)):
            if rungs[i]-rungs[i-1]>dist:
                cnt+= (rungs[i]-rungs[i-1]-1)//dist
        
        return cnt