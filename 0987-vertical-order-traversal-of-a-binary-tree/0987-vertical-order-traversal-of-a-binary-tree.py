# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## depends on the left displacement as well as the depth
        dic = defaultdict(list)
        def recur(placement,depth,node,dic):
            if not node:
                return
            dic[placement].append((depth,node.val))
            
          
            recur(placement-1,depth+1,node.left,dic)
            recur(placement+1,depth+1,node.right,dic)                
        
        recur(0,0,root,dic) #(placement, depth, root)
        ans =[]
        for idx in sorted(dic.keys()):
            temp=[]
            for j in sorted(dic[idx]):
                temp.append(j[1])
            ans.append(temp)
        return ans