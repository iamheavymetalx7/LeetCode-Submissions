class Solution:
    def solve(self,board,word,i,j,count):
        length=len(word)
        
        if count>=length:
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[count]:
            return False
        board[i][j]='$'
        a=self.solve(board,word,i-1,j,count+1)
        b=self.solve(board,word,i+1,j,count+1)
        c=self.solve(board,word,i,j-1,count+1)
        d=self.solve(board,word,i,j+1,count+1)
        board[i][j]=word[count]
        
        return (a or b or c or d)

        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                x=False
                if board[i][j]==word[0]:
                    x = self.solve(board,word,i,j,0)
                if x:
                    return True
        return False
                    
        