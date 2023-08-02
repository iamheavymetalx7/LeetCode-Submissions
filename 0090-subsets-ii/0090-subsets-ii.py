class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        n=len(nums)
        nums.sort()
        def recur(idx,arr):
            ans.append(arr.copy())
            
            
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                
                arr.append(nums[i])
                recur(i+1,arr)
                arr.pop()
        recur(0,[])
        return ans