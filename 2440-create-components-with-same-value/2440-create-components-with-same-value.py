## def dfs post order traversal, links for both solutions used:
'''
1.https://leetcode.com/problems/create-components-with-same-value/discuss/2706736/Python-Explanation-with-pictures-BFS
https://leetcode.com/problems/create-components-with-same-value/discuss/2707304/Python3-post-order-dfs
'''
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        
        tree =[[] for _ in range(len(nums))]
        
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        
        def fn(u,p):
            ans = nums[u]
            
            for v in tree[u]:
                if v!=p:
                    ans+=fn(v,u)
            return 0 if cand == ans else ans
        
        def divisors(x):
            div =[]
            for i in range(1,int(math.sqrt(x))+1):
                if x%i==0:
                    div.append(i)
                if x//i!=i:
                    div.append(x//i)
            return sorted(div)
        
        summ= sum(nums)
        
        possible = divisors(summ)
        
        for cand in possible:
            if summ%cand==0 and fn(0,-1)==0:
                return summ//cand -1