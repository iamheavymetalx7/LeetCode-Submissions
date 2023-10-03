class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        arr=[]
        
        n,m = len(forest),len(forest[0])
        
        for i in range(n):
            for j in range(m):
                if forest[i][j]>1:
                    arr.append([forest[i][j],i,j])
        
        arr.sort()
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        def bfs(forest,cur_row,cur_col,end_row,end_col):
            if cur_row ==end_row and cur_col == end_col:
                return 0
            
            q=deque()
            vis =set()
            q.append([cur_row,cur_col])
            vis.add((cur_row,cur_col))
            step=0
            while q:
                step+=1
                new_len=len(q)
                
                
                for j in range(new_len):
                    sr,sc = q.popleft()
                    for dx,dy in dire:
                        dx+=sr
                        dy+=sc
                        
                        if dx<0 or dx>=n or dy<0 or dy>=m or (dx,dy) in vis or forest[dx][dy]==0:
                            continue

                        if dx==end_row and dy==end_col:
                            return step
                        q.append([dx,dy])
                        vis.add((dx,dy))
            return -1
        
        ans =0
        cur_row,cur_col =0,0
        ans = 0
        for i in range(len(arr)):
            steps = bfs(forest,cur_row,cur_col,arr[i][1],arr[i][2])
            if steps==-1:
                return -1
            ans+=steps
            cur_row,cur_col = arr[i][1],arr[i][2]
        
        return ans
        