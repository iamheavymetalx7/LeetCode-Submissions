class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        
        ans =[]
        
        #[11256710]
        
        def recur(idx,tt,arr):
            if tt<0:
                return
            if tt==0:
                ans.append(arr.copy())
            
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                
                recur(i+1,tt-nums[i],arr+[nums[i]])
                
                
            
        
        
        
        recur(0,target,[])
        
        return ans
        