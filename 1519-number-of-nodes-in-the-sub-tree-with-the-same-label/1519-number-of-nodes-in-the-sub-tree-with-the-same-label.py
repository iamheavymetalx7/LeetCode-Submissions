from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(list)
        
        for p,c in edges:
            adj_list[p].append(c)
            adj_list[c].append(p)

        labels=list(labels)
        counter=[0]*26
        ans=[0]*n
        
        vis=set([0])
        
        
        def dfs(node):
            nodeLabelId = ord(labels[node])-ord('a')
            # save to temporary variable amount of nodes with label same as is for current node.
            # Everything that will be added for this nodeLabelId after, will counts as subtree of this node.
            before = counter[nodeLabelId]
            counter[nodeLabelId]+=1
            
            for nei in adj_list[node]:
                if nei in vis:
                    continue
                vis.add(nei)
                dfs(nei)
            # Set the result for the current node:
            # everything that was added after we saved the "before" variable was added from subtree of this node.
            ans[node]=counter[nodeLabelId]-before
            return counter
                        
        dfs(0)
                        
        return ans
            
            
            
            

                