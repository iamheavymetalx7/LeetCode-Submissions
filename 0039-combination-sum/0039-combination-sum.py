class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n =len(nums)
        
        ans =[]
        def recur(idx,arr,tt):
            if tt ==0:
                ans.append(arr.copy())
                return
            if tt<0 or idx>=n:
                return 
            take = recur(idx,arr+[nums[idx]],tt-nums[idx])
            
            nottake = recur(idx+1,arr,tt)
        
        recur(0,[],target)
        
        return ans
            