class Solution:
    ##BFS approach
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         subsets=[[]]
        
        
#         for num in nums:
#             n=len(subsets)
#             for i in range(n):
#                 set1=list(subsets[i])
#                 set1.append(num)
#                 subsets.append(set1)
#         return subsets

##  Recursive approach
     def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subset =[]
        
        def helper(index,sub):
            if index>=n:
                subset.append(sub)
            else:
                helper(index+1, sub+[nums[index]])
                helper(index+1,sub)
        helper(0,[])
        return subset
