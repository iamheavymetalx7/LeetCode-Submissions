class Solution:
    def searchMatrix(self,  mat: List[List[int]], target: int) -> bool:
        n,m=len(mat),len(mat[0])
        
        l=-1
        r=n*m
        
        while r-l>1:
            mid = (l+r)//2
            
            if target>=mat[mid//m][mid%m]:
                l = mid
            else:
                r=mid
        if mat[l//m][l%m]==target:
            return True
        return False
                