'''
binary search. + dfs
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        l=-1
        r=10**6+1
        
        n,m=len(heights),len(heights[0])
        dire=[(1,0),(0,1),(-1,0),(0,-1)]

        def check(mid):
            vis=set()
            
            def dfs(r,c,mid):
                if r==n-1 and c==m-1:
                    return True
                vis.add((r,c))
                for dx,dy in dire:
                    dx+=r
                    dy+=c
                    if 0<=dx<n and 0<=dy<m and (dx,dy) not in vis:
                        if abs(heights[dx][dy]-heights[r][c])<=mid:
                            if dfs(dx,dy,mid):
                                return True
                return False
            
            return dfs(0,0,mid)
                
                
            
        
        while r-l>1:
            mid =(l+r)//2
            
            if check(mid):
                r=mid
            else:
                l=mid
        return r