class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        
        n=len(nums)
        ans=[]
        
        nums.sort()
        
        def recur(idx,tt,arr):
            if tt ==0:
                ans.append(arr.copy())
                return
            if tt<0:
                return
            
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                
                arr.append(nums[i])
                recur(i+1,tt-nums[i],arr)
                arr.pop()
        recur(0,target,[])
        
        return ans
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ___________________ IGNORE - WRONG CODE _______________________________________       
# class Solution:
#     def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
#         n=len(nums)
#         ans =[]
#         nums.sort()
        
#         print(nums)
        
#         def recur(idx,arr,tt):
            
#             if tt==0:
#                 ans.append(arr.copy())
#                 return
#             if idx>=n or tt<0:
#                 return           
#             # if idx>0 and nums[idx]==nums[idx-1]:
                
#             take = recur(idx+1,arr+[nums[idx]],tt-nums[idx])
#             nottake = recur(idx+1,arr,tt)
        
#         recur(0,[],target)
#         return ans
            