class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr=set()
        n=len(nums)
        def recur(index,ans):
            if index>=len(nums):
                if len(ans)>=2:
                    arr.add(tuple(ans))
                return
            if len(ans)==0 or nums[index]>=ans[-1]:
                recur(index+1,ans+[nums[index]])
            
            recur(index+1, ans)
        
        for i in range(len(nums)):
            recur(i,[])
        
        return list(arr)
