class Solution:
    def totalNQueens(self, n: int) -> int:
        
        nQueens = [["." for i in range(n)] for i in range(n)]
    
        
        def isValid(row,col):
            for i in range(n):
                if i!=row:
                    if nQueens[i][col]=="Q":

                        return False
            i,j=row-1,col-1 
            while i>=0 and j>=0:
                    if nQueens[i][j]=="Q":
                        return False
                    i-=1
                    j-=1
            
            i,j = row-1,col+1
            while i>=0 and j<n:
                if nQueens[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
        
        ans =[0]
        
        def solveNqueens(row):
            if row==n:
                
                ans[0]+=1
            
            for col in range(n):
                if isValid(row,col):

                    nQueens[row][col]="Q"
                    solveNqueens(row+1)
                    nQueens[row][col]="."
        solveNqueens(0)
        
        return (ans[0])
            
            
        
                                
                        
                        
                            
