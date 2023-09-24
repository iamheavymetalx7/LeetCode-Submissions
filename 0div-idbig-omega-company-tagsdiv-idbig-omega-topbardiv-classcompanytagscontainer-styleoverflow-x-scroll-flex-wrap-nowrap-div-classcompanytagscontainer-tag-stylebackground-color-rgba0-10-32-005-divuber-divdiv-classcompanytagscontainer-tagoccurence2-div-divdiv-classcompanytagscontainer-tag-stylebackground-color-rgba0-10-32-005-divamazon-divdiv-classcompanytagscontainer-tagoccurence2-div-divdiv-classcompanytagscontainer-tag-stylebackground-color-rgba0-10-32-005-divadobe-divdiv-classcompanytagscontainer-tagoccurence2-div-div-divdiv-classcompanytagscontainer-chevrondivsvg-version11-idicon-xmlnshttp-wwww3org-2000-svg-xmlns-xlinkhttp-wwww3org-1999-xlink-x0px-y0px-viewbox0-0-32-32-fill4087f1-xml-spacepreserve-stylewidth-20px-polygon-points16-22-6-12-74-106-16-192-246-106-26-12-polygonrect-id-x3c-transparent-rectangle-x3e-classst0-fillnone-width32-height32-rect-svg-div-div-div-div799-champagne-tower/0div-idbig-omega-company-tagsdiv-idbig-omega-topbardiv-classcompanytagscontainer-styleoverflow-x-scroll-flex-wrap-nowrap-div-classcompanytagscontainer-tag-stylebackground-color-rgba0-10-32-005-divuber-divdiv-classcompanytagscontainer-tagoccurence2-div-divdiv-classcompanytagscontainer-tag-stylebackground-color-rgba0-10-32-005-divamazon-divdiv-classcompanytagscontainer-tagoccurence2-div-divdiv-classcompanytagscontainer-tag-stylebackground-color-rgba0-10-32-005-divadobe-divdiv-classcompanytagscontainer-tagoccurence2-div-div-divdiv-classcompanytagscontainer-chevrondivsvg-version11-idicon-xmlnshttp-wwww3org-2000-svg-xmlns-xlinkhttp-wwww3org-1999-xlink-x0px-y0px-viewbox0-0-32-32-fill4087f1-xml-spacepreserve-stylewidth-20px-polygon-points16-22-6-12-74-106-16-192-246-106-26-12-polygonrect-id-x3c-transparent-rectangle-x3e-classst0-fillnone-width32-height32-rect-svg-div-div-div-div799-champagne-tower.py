class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        prev_row = [poured]
        
        
        for i in range(1,query_row+1):
            cur_row = [0]*(i+1)
            
            for j in range(i):
                extra = prev_row[j]-1
                if extra>0:
                    cur_row[j]+=0.5*extra
                    cur_row[j+1]+=0.5*extra
            
            prev_row = cur_row
        
        return min(prev_row[query_glass],1)
    