class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_count = senate.count("R")
        d_count = len(senate)- r_count
        
        d_ban=0
        r_ban=0
        
        q= deque(senate)
        
        
        while r_count and d_count:
            
            curr=q.popleft()
            
            if curr=="D":
                if d_ban:
                    d_ban-=1
                    d_count-=1
                else:
                    r_ban+=1
                    q.append("D")
            else:
                if r_ban:
                    r_ban-=1
                    r_count-=1
                else:
                    d_ban+=1
                    q.append("R")
        
        return "Radiant" if r_count else "Dire"