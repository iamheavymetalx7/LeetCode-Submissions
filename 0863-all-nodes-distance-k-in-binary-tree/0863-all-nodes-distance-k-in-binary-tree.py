# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
#         def dfs(node):
#             if not node:
#                 return
            
#             if node.left:
#                 graph[node.val].append(node.left.val)
#                 graph[node.left.val].append(node.val)
#                 dfs(node.left)
#             if node.right:
#                 graph[node.val].append(node.right.val)
#                 graph[node.right.val].append(node.val)
#                 dfs(node.right)
        
#         dfs(root)
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
        
        print(graph)
        
        
        q=deque()
        q.append([target.val,0])
        vis=set()
        ans=[]
        
        while q:
            node,dist = q.popleft()
            vis.add(node)
            if dist ==k:
                ans.append(node)
                
            
            
            for nei in graph[node]:
                if nei not in vis:
                    q.append([nei,dist+1])
        
        return ans
            
                