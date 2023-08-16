class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap =[]
        n,m =len(matrix),len(matrix[0])
        
        ## element, row,col
        for i in range(min(k,m)):
            heappush(heap,[matrix[i][0],i,0])
        
        for i in range(k):
            val,row,col = heappop(heap)
            
            if col+1<m:
                heappush(heap,[matrix[row][col+1],row,col+1])
        return val