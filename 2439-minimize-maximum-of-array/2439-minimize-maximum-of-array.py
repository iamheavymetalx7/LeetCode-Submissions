# class Solution:
#     def minimizeArrayValue(self, nums: List[int]) -> int:
        
#         def isPossible(val,arr):
#             # print(arr)
#             n=len(arr)
#             for i in range(n-1):
#                 if arr[i]>val:
#                     return False
#                 arr[i+1]-=(val-arr[i])
                
#             return arr[-1]<=val
        
#         l=-1
#         r=10**9+5
        
#         while r>l+1:
#             m=(l+r)//2
#             b=nums.copy()
            
#             if isPossible(m,b):
#                 r=m
#             else:
#                 l=m
#         return r
            
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res=nums[0]
        
        total=nums[0]
        
        n=len(nums)
        
        for i in range(1,n):
            total+=nums[i]
            res=max(res, math.ceil(total/(i+1)))
        
        return res
        