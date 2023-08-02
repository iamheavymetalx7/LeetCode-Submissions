class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)
        ans =[]
        
        vis = [0]*(n)
        
        
        def recur(arr):
            if len(arr)==n:
                ans.append(arr.copy())
                return
            
            for i in range(n):
                if vis[i]:
                    continue
                arr.append(nums[i])
                vis[i]=1
                recur(arr)
                vis[i]=0
                arr.pop()
                
        recur([])
        
        return (ans)