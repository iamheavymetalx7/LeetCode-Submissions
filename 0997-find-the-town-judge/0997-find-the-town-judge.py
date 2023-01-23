class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count=[0]*(n+1)
        
        if n==1 and len(trust)==0:
            return 1
        
        for x,y in trust:
            # print(x,y)
            count[x]-=1
            count[y]+=1
        
        for i in range(n+1):
            if count[i]==n-1:
                return i
        
        return -1
        