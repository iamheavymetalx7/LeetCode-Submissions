class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            childs =set(leftChild)|set(rightChild)
            
            for i in range(n):
                if i not in childs:
                    return i
            return -1
        
        root = find_root()
        if root==-1:
            return False
        
        q = deque()
        q.append(root)
        seen=set()
        seen.add(root)
        
        while q:
            node = q.popleft()
            for c in [leftChild[node],rightChild[node]]:
                if c!=-1:
                    if c in seen:
                        return False
                    
                    q.append(c)
                    seen.add(c)
        return len(seen)==n
                    