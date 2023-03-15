class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        n=len(nums)
        # print(n)
        i=0
        j=n//2
        cnt=0
        
        marked=[False]*n
        
        while i<n//2:
            while j<n and 2*nums[i]>nums[j]:
                j+=1
            
            if j<n:
                marked[i]=True
                marked[j]=True
                i+=1
                j+=1
            else:
                break
        
        for i in range(n):
            if marked[i]:
                cnt+=1
        return cnt
    