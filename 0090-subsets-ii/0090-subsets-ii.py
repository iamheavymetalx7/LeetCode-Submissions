class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans=[]
#         ds=[]
        
        
#         def helper(index,ds):
#             ans.append(ds)  
#             for i in range(index,len(nums)):
#                 if i!=index and nums[i]==nums[i-1]:
#                     continue
#                 helper(index+1,ds+[nums[i]])
                
#         helper(0,ds)
#         return ans
                        
                        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        nums.sort()
        
            
        def recursion(idx,ds):
            ans.append(ds)
            for i in range(idx,len(nums)):
                if i!=idx and nums[i]==nums[i-1]:
                    continue
                recursion(i+1,ds+[nums[i]])

        
        recursion(0,ds)
        return ans
        