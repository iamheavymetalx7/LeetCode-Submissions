class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        i,j=0,0
        vis =set()

        matrix =[[0]*(n) for _ in range(n)]
        cur =1
        n,m=len(matrix),len(matrix[0])
        
        right,up,down,left = True,False,False,False
        
        while len(vis)!=(m*n):
            matrix[i][j]=cur
            vis.add((i,j))
            cur+=1
            
            if right:
                if j+1<m and (i,j+1) not in vis:
                    j+=1
                else:
                    right=False
                    down=True
                    i+=1
                    continue
            if down:
                if i+1<n and (i+1,j) not in vis:
                    i+=1 
                else:
                    down=False
                    left=True
                    j-=1
                    continue
            if left:
                if j-1>=0 and (i,j-1) not in vis:
                    j-=1
                else:
                    left=False
                    up=True
                    i-=1
                    continue
            if up:
                if i-1>=0 and (i-1,j) not in vis:
                    i-=1  
                else:
                    right=True
                    up=False
                    j+=1
                    continue
        return matrix
                    
                