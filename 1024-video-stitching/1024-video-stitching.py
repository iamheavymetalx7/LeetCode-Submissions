class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x:x[0])
        
        # print(clips)
        ## i think it is based on take - nottake scenario
        ## if we take, we are taking where last_end>=first_curr
        
        n=len(clips)
        
        @cache
        def recur(idx,last):
            
            if idx>=n:
                if last>=time:
                    return 0
                return int(1e19)
            
            ans = int(1e19)
            
            ## take case
            if last>=clips[idx][0]:
                ans=min(1+recur(idx+1,clips[idx][1]),ans)
            
            ## not take case
            ans = min(ans,recur(idx+1,last))
            
            return ans
        
        val = recur(0,0)
        
        if val == int(1e19):
            return -1
        return val
        
            
                