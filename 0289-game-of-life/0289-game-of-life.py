class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ## lc -> live count
        
        ## if b[i][j]=1 and lc<2 or lc>3 : -1
        ## if baord[i][j]=1 and lc==2 or lc==3 :  no need to update/change
        ## if not b[i][j] and lc==3: 2
        
        dire =[(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]
        
        n,m=len(board),len(board[0])
        for i in range(n):
            for j in range(m):
                
                lc =0
                
                for dx,dy in dire:
                    dx+=i
                    dy+=j
                    if 0<=dx<n and 0<=dy<m and abs(board[dx][dy])==1:
                        lc+=1
                
                if board[i][j]:
                    if lc>3 or lc<2:
                        board[i][j]=-1
                else:   ## deadcell
                    if lc==3:
                        board[i][j]=2
        
        for i in range(n):
            for j in range(m):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
        