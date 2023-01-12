class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        n_mat= mat.copy()
        for j in range(4):
            if n_mat == target:
                return True
            
            for i in range(n):
                for j in range(i):
                    n_mat[i][j], n_mat[j][i] = n_mat[j][i], n_mat[i][j]
            
            for row in n_mat:
                row.reverse()
        return False
            