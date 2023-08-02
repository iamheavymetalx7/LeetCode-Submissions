class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        n=len(nums)
        
        vis =[0]*(n)
        
        
        def recur(idx,arr):
            
            if len(arr)==n:
                ans.append(arr.copy())
                return
            
            for i in range(n):
                if vis[i]:
                    continue
                
                arr.append(nums[i])
                vis[i]=1
                recur(i+1,arr)
                vis[i]=0
                arr.pop()
        recur(0,[])
        return ans
                    
                
        