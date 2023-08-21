class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        group_id = m
        for i in range(n):
            if group[i]==-1:
                group[i] = group_id
                group_id+=1
        
        item_graph=[[] for _ in range(n)]
        group_graph = [[] for _ in range(group_id)]
        item_indegree=[0]*(n)
        group_indegree=[0]*(group_id)
        
        
        for i,ele in enumerate(beforeItems):
            for j in ele:
                item_graph[j].append(i)
                item_indegree[i]+=1
                
                
                if group[i]!=group[j]:
                    group_graph[group[j]].append(group[i])
                    group_indegree[group[i]]+=1
                    

        def topo(graph,indegree):
            toposort= []
            q=deque()
            
            for node in range(len(graph)):
                if indegree[node]==0:
                    q.append(node)
                    

            while q:
                node =q.popleft()
                toposort.append(node)
                for adj in graph[node]:
                    indegree[adj]-=1
                    if indegree[adj]==0:
                        q.append(adj)
            return toposort if len(graph)==len(toposort) else []
        
        item_order = topo(item_graph,item_indegree)
        group_order = topo(group_graph, group_indegree)
        
        print(item_order,"item_order")
        print(group_order,"group_order")
        
        if not item_order or not group_order:
            return []
        
        ordered_groups = defaultdict(list)
        
        ## har individual group me jo order h wo ye maintain kr rha h
        for item in item_order:
            ordered_groups[group[item]].append(item)
        
        ans= []
        
        ## har group ka jo order h, wo ye maintain kr lega, internally taken care of and now externally take care kr rhe h
        
        for group_idx in group_order:
            ans += ordered_groups[group_idx]
        return ans