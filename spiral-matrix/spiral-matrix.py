class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i,j=0,0
        vis =set()
        arr= []
        n,m=len(matrix),len(matrix[0])
        
        right,up,down,left = True,False,False,False
        
        while len(vis)!=(m*n):
            arr.append(matrix[i][j])
            vis.add((i,j))
            
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
        return arr
                    
                
                
            