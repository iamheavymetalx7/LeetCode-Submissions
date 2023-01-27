class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length =len(board)
        
        board.reverse()
        
        def IntPos(square):
            r = (square-1)//length
            
            c =  (square-1) % length
            
            if r%2==1:
                c = length-1-c
            
            return [r,c]
                
            
            
        
        
        q=deque()
        q.append([1,0])
        #represents square, moves
        
        vis=set()
        
        while q:
            sq,moves = q.popleft()
            
            for nxtsq in range(sq+1,sq+7):
                r,c = IntPos(nxtsq)
                     
                # nxtsq= board[r][c]
                if board[r][c]!=-1:
                    nxtsq=board[r][c]
                    
                if nxtsq==length*length:
                    return moves+1
                if nxtsq not in vis:
                    vis.add(nxtsq)
                    q.append([nxtsq,moves+1])
                    
        return -1
                
        