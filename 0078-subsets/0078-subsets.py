class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        n=len(nums)
        def recur(idx,arr):
            ans.append(arr.copy())
            
            for i in range(idx,n):
                arr.append(nums[i])
                recur(i+1,arr)
                arr.pop()
        
        recur(0,[])
        
        return ans