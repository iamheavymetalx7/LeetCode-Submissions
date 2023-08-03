'''
https://leetcode.com/problems/n-queens/discuss/1564825/Simple-Python-Solution-Using-Backtracking

https://leetcode.com/problems/n-queens/discuss/19808/Accepted-4ms-c%2B%2B-solution-use-backtracking-and-bitmask-easy-understand.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
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
        
        ans =[]
        
        def solveNqueens(row):
            if row==n:
                
                ans.append(["".join(i) for i in nQueens])
                return
            
            for col in range(n):
                if isValid(row,col):

                    nQueens[row][col]="Q"
                    solveNqueens(row+1)
                    nQueens[row][col]="."
        solveNqueens(0)
        
        return (ans)
            
            
        
                                
                        
                        
                            
