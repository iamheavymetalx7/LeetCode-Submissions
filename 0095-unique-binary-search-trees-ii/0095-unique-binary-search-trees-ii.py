# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        @cache
        def recur(left,right):
            if left>right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            
            ans =[]
            for root in range(left,right+1):
                leftNodes = recur(left,root-1)
                rightNodes = recur(root+1,right)

                for leftN in leftNodes:
                    for rightN in rightNodes:
                        rootNode = TreeNode(root,leftN,rightN)
                        
                        ans.append(rootNode)
                        
            return ans
                
            
        return recur(1,n)