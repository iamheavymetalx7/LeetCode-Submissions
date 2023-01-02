# The idea: what if we iterate through all the boarder O's and preserve all the connected O's.

# We use BFS here!
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        q=deque()
        
        for i in range(n):
            if board[i][0]=='O':
                q.append((i,0))
            if board[i][m-1]=="O":
                q.append((i,m-1))
                
        for j in range(m):
            if board[0][j]=="O":
                q.append((0,j))
            if board[n-1][j]=="O":
                q.append((n-1,j))
        
        
        while q:
            x,y = q.popleft()
            
            board[x][y]="#"
            
            for xx, yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=xx<n and 0<=yy<m:
                    if board[xx][yy]!="O" :
                        continue
                    q.append((xx,yy))
                    board[xx][yy]='#'
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]="O"
                    