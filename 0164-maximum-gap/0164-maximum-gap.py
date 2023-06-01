class Solution:
    def maximumGap(self, a: List[int]) -> int:
        n=len(a)
        mini = min(a)
        maxi=max(a)
        
        if n==1:
            return 0
        gap = (maxi-mini)/(n-1)
        if gap<1.0: 
            gap=1.0
        # print(gap)
        vector = [[1e11,-1] for _ in range(n)]
        
        for i in range(n):
            pos = int((a[i] - mini)/gap)
            
            vector[pos][0] = min(a[i],vector[pos][0])
            vector[pos][1] = max(a[i],vector[pos][1])
        res=0
        print(gap)
        print(vector)
        prevMax = vector[0][1]
        
        for i in range(1,n):
            if vector[i][0]==1e11:
                continue
            res=max(res,vector[i][0]-prevMax)
            prevMax = vector[i][1]        
        return res
            
        