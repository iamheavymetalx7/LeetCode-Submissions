class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(speed)
        time=[(dist[i]*10**8)/speed[i] for i in range(n)]
        
        a=[]
        for i,x in enumerate(time):
            a.append([x,i])
        a.sort()
        
        # print(a)
        cnt=0
        time=0
        for i in range(n):
            # print(dist[a[i][1]]-time*speed[a[i][1]])
            if dist[a[i][1]]-time*speed[a[i][1]]>0:
                cnt+=1
            else:
                return cnt
            time+=1
        return cnt