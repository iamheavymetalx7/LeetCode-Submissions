'''
hint: https://leetcode.com/problems/snakes-and-ladders/discuss/3092663/Beats-100(2ms)-ororEasy-SolutionsororFully-Explainedoror-C%2B%2Boror-Javaoror-Python3
'''

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def label_to_pos(x):
            r,c = divmod(x-1,n)
            
            if r%2==0:
                r,c = n-r-1,c
            else:
                r,c = n-r-1,n-c-1
            
            return (r,c)
        
        
        q=deque()
        
        vis=set()
        q.append((1,0))     ## label, moves
        
        
        while q:
            sq,mv = q.popleft()
            
            ## since no snakes/ladder on 0 or last, we can start by assuming dice is thrown
            
            
            for newsq in range(sq+1,sq+7):
                r,c = label_to_pos(newsq)
                
                if board[r][c]!=-1:
                    newsq = board[r][c]
                
                if newsq == n**2:
                    return mv+1
                
                if newsq not in vis:
                    vis.add(newsq)
                    q.append((newsq,mv+1))
        return -1
                    
                