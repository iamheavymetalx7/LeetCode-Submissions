from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree=defaultdict(list)
        
        def dfs(node):
            if not node:
                return "null"
            
            
            s = ",".join([str(node.val),dfs(node.left), dfs(node.right)])
            print(s)
            if len(subtree[s])==1:
                res.append(node)
            subtree[s].append(node)
        
            return s
            
        
        res=[]
        dfs(root)
        
        # print(subtree)

        return res 