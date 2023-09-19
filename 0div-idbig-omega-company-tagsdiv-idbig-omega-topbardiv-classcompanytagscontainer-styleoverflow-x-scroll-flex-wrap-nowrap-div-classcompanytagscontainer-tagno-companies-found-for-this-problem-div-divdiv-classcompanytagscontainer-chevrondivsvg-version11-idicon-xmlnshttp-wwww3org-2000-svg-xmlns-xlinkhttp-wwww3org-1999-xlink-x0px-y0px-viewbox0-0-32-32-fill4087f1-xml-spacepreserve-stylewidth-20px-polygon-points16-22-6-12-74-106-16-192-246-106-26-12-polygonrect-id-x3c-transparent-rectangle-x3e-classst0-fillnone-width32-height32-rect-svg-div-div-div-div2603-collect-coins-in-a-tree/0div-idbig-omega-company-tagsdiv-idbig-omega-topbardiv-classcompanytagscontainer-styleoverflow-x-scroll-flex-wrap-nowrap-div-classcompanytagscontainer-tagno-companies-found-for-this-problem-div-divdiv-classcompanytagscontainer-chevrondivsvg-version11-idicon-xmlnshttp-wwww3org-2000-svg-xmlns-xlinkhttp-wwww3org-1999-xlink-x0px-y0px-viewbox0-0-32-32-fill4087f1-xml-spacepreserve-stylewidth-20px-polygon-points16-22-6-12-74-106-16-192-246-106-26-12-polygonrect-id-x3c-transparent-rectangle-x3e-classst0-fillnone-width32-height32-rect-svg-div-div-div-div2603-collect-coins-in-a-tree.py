'''
https://leetcode.com/submissions/detail/922363126/

https://www.youtube.com/watch?v=wUmuRsTGQxs

because we are modyifng lists, we are passing the list to functions as list[x][:]

and also for min_time_for_subroot instead of [0 for _ in range(N)] we use
[[0] for _ in range(N)]

'''

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n=len(coins)
        
        def mergecoins(tgt,src):
            tgt[1]+=src[0]
            tgt[2]+=src[1]
            tgt[3]+=src[2]+src[3]
        
        def removecoins(tgt,src):
            tgt[1]-=src[0]
            tgt[2]-=src[1]
            tgt[3]-= (src[2]+src[3])
        
        def removemintime(target_min_time,src_coins,src_min_time):
            if ((src_coins[2]+src_coins[3])>0):
                target_min_time[0] -=(2+src_min_time[0])
        
                
                
        def mergemintime(target_min_time,src_coins,src_min_time):
            if ((src_coins[2]+src_coins[3])>0):
                target_min_time[0] +=(2+src_min_time[0])
        
            
            
        min_time_for_subtree = [[0] for _ in range(n)]
        min_time_for_root = [[0] for _ in range(n)]
        cnt_coins_subtree = [[0]*(4) for _ in range(n)]
        cnt_coins_root = [[0]*(4) for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        has_coins = [coins[i] for i in range(n)]
        

        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        def dfs_in(src,par):
            for child in graph[src]:
                if child==par:continue
                    
                dfs_in(child,src)
                
                mergecoins(cnt_coins_subtree[src],cnt_coins_subtree[child])
                mergemintime(min_time_for_subtree[src],cnt_coins_subtree[child],min_time_for_subtree[child])
                    
                
            if has_coins[src]:
                cnt_coins_subtree[src][0]=1
                
        def dfs_out(root,par):
            for child in graph[root]:
                if child==par:
                    continue
                
                cnt_coins_except_child = cnt_coins_root[root][:]
                removecoins(cnt_coins_except_child, cnt_coins_subtree[child])
                
                min_time_except_child = min_time_for_root[root][:]
                removemintime(min_time_except_child,cnt_coins_subtree[child],min_time_for_subtree[child])
                
                ## now we calc the value when "child" becomes the "root"
                
                cnt_coins_root[child] = cnt_coins_subtree[child][:]
                mergecoins(cnt_coins_root[child],cnt_coins_except_child)
                
                min_time_for_root[child] = min_time_for_subtree[child][:]
                mergemintime(min_time_for_root[child],cnt_coins_except_child,min_time_except_child)
            
                dfs_out(child,root)
                
        dfs_in(0,-1)

        
        cnt_coins_root[0] = cnt_coins_subtree[0][:]
        min_time_for_root[0] = min_time_for_subtree[0][:]
        print(min_time_for_subtree)

        
        dfs_out(0,-1)
        print(min_time_for_root)
        
        
        res = int(1e20)
        
        for i in range(n):
            res = min(res, min_time_for_root[i][0])
        return res
        
                
