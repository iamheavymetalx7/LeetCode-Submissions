class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        
        presumRow = [[0]*(m+1) for _ in range(n)]
        presumCol = [[0]*(n+1) for _ in range(m)]
        
        
        for r in range(n):
            for c in range(m):
                presumRow[r][c+1] = presumRow[r][c]+grid[r][c]
                presumCol[c][r+1] = presumCol[c][r]+grid[r][c]
                
        def getsumRow(row,l,r):
            return presumRow[row][r+1]-presumRow[row][l]
        def getsumCol(col,l,r):
            return presumCol[col][r+1]-presumCol[col][l]
        
        def check(k):
            for r in range(n-k+1):
                for c in range(m-k+1):
                    diag,anti =0,0
                    for d in range(k):
                        diag+=grid[r+d][c+d]
                        anti+=grid[r+d][c+k-1-d]
                    nr,nc =r,c
                    match = (diag == anti)
                    while nr<r+k and match:
                        match = (diag ==(getsumRow(nr,c,c+k-1)))
                        nr+=1
                    while nc<c+k and match:
                        match = (diag==(getsumCol(nc,r,r+k-1)))
                        nc+=1
                    if match:
                        return True
            return False
                        
        
        
        for k in range(min(m,n),1,-1):
            if check(k):
                return k
        return 1