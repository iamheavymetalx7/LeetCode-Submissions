class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n =len(nums)
        
        print(nums)
        
        ans =[]
        
        def recur(idx,arr,tt):
            if tt ==0:
                ans.append(arr.copy())
                return
            if tt<0:
                return 
            for i in range(idx,n):
                arr.append(nums[i])
                recur(i,arr,tt-nums[i])
                arr.pop()        
        recur(0,[],target)
        
        return ans
            