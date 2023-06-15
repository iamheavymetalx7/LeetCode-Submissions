# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxi, level, maxLevel = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            summ = 0
            for _ in range(len(q)):
                node = q.popleft()
                summ += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxi < summ:
                maxi, maxLevel = summ, level        
        return maxLevel