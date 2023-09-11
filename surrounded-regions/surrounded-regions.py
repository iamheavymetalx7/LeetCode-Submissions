class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board);m=len(board[0])
        
        dire= [(0,1),(1,0),(-1,0),(0,-1)]
        
        q=deque()
        
        for i in range(n):
            if board[i][0]=="O":
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
            
            for dx,dy in dire:
                dx+=x
                dy+=y
                if 0<=dx<n and 0<=dy<m and board[dx][dy]=="O":
                    q.append((dx,dy))
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]="O"