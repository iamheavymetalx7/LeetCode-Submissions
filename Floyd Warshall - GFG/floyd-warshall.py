#User function template for Python

class Solution:
	def shortest_distance(self, mat):
		#Code here
		
		n,m=len(mat),len(mat[0])

        for i in range(n):
            for j in range(n):
                if mat[i][j]==-1:
                    mat[i][j]=int(1e9)
                if i==j:
                    mat[i][j]=0
                    
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j]= min(mat[i][j], mat[i][k]+mat[k][j])
        
        
        
        
        for i in range(n):
            if mat[i][i]<0:
                print("contains negative cycle")
        
        for i in range(n):
            for j in range(n):
                if mat[i][j]==int(1e9):
                    mat[i][j]=-1

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends