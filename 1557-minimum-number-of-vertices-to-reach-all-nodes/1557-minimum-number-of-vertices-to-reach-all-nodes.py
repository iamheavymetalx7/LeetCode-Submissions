class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for src,dst in edges:
            graph[dst].append(src)
            
        ans=[]
        
        for i in range(n):
            if not graph[i]:
                ans.append(i)
                
        return ans
        

                    
            
        