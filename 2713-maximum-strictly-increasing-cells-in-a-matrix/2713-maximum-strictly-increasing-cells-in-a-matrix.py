class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n,m=len(mat),len(mat[0])
        
        distinct =set()
        dic = defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                dic[mat[i][j]].append([i,j])
                distinct.add(mat[i][j])
        
        rows = [0]*(n)
        cols = [0]*(m)
        
        distinct = sorted(distinct)
        # print(distinct)
        
        for cur in distinct:
            arr =[]
            
            for pr,pc in dic[cur]:
                arr.append([max(rows[pr],cols[pc])+1,pr,pc])
            
            
            for maxi,r,c in arr:
                rows[r]=max(rows[r],maxi)
                cols[c]=max(cols[c],maxi)
        
        
        return max(max(rows),max(cols))
                