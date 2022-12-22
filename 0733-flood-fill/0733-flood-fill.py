class Solution:
    def dfs(self,i,j,oclr,nclr,image):
        n=len(image)
        m=len(image[0])
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        image[i][j]=nclr
        
        
        for x,y in dire:
            if 0<=i+x<n and 0<=j+y<m and image[i+x][j+y]==oclr:
                self.dfs(i+x,j+y,oclr,nclr,image)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        clr = image[sr][sc]
        
        if clr!=color:
            self.dfs(sr,sc,clr,color,image)

        return image
        