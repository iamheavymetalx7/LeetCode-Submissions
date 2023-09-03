'''
recursion gives tle, we use bfs code, where we visit each index only once
https://leetcode.com/problems/jump-game-vii/discuss/1224654/Clean-Python-3-BFS
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        mx =0
        
        q = deque()
        q.append(0)
        
        while q:
            idx = q.popleft()
            
            for j in range(max(idx+minJump,mx+1),min(idx+maxJump+1,len(s))):
                if s[j]=="0":
                    if j==len(s)-1:
                        return True
                    q.append(j)
            mx = idx+maxJump
        return False
                    
        