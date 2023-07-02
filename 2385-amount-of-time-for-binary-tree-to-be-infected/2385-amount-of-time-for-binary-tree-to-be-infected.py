# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        q= deque()
        
        q.append(root)
        
        graph = defaultdict(list)
        
        while q:
            node = q.popleft()
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        
        vis=set()
        t=0
        q.append((start,t))
        
        
        maxi =0
        while q:
            ele,t = q.popleft()
            if ele in vis:
                continue
            else:
                vis.add(ele)
            maxi=max(maxi,t)
            for nei in graph[ele]:
                q.append((nei,t+1))
        
        return maxi
        
        
        
        