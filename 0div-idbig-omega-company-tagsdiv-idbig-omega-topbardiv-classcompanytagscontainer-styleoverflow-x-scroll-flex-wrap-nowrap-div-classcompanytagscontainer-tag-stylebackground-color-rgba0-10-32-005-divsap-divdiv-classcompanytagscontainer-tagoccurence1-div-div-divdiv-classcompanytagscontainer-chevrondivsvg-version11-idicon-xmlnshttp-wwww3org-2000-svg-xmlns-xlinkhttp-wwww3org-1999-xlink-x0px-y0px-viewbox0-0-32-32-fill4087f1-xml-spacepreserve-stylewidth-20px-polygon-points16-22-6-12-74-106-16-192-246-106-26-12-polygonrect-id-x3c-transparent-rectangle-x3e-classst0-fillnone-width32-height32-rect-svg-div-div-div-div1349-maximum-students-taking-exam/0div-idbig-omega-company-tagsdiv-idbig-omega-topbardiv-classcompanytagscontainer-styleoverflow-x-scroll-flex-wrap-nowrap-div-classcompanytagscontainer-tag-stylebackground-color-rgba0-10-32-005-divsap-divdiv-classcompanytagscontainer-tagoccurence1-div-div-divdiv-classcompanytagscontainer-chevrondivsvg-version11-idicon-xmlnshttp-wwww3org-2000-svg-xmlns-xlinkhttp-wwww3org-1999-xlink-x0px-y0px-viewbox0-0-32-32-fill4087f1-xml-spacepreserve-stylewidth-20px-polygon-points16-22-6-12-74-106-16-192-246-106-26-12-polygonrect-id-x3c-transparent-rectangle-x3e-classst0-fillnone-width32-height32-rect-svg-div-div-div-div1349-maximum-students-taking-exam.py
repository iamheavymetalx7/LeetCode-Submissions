class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
        n,m = len(seats), len(seats[0])
        
        def check(mask,idx):
            if idx<0:
                return True
            if mask&(1<<idx)==0:
                return True
            return False
        @cache
        def recur(row,j,prev,curr):
            if row>=n:
                return 0
            
            ans = -1
            
            if check(prev,j-1) and check(prev,j+1) and check(curr,j-1) and seats[row][j]!="#":
                if j==m-1:  ## if it is the last column
                    ans = max(ans,1+recur(row+1,0,curr|(1<<j),0))
                else:
                    ans = max(ans,1+recur(row,j+1,prev,curr|(1<<j)))
            
            # now we do the not take case
            if j==m-1:
                ans=max(ans, recur(row+1,0,curr,0))
            else:
                ans=max(ans,recur(row,j+1,prev,curr))
            
            return ans
            
        val = recur(0,0,0,0)
        return val