class Solution:
    
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        print(len(time))
        def findTrips(m,time):
            cnt= 0 
            for i in range(len(time)):
                cnt+=m//(time[i])
            
            # print(cnt,m,totalTrips)
            
            if cnt>=totalTrips:
                return True
            
            return False
            
        
        
        l,r=-1,int(1e20)
        
        while r>l+1:
            m=(l+r)//2
            ans = findTrips(m,time)
            if ans:
                r=m
            else:
                l=m
        return r
        