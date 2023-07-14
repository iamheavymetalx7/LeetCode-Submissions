class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        vis=set()
        n=len(arr)
        
        q=deque()
        q.append(start)

        while q:
            curr = q.popleft()
            
            if arr[curr]==0:
                return True
            
   
            next1 = curr+arr[curr]
            
            if next1<=n-1 and next1 not in vis:
                q.append(next1)
            
            next2= curr-arr[curr]
            if next2>=0 and next2 not in vis:
                q.append(next2)
            
            vis.add(curr)
        return False
                
                