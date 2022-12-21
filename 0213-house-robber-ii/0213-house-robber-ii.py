class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        temp1=[nums[i] for i in range(len(nums)-1)]
        temp2 =[nums[i] for i in range(1,len(nums))]
        
        if len(nums)==1:
            return nums[0]
        
        
        dp1=[-1]*(len(temp1))
        
        def recur(index,arr):
            if index>=len(arr):
                return 0
            if dp1[index]!=-1:
                return dp1[index]
            
            take = recur(index+2,arr)+arr[index]
            nottake = recur(index+1,arr)
            
            dp1[index] = max(take, nottake)
            
            return dp1[index]
        
        dp2=[-1]*len(temp2)
        
        def recur2(index,arr):
            if index>=len(arr):
                return 0
            if dp2[index]!=-1:
                return dp2[index]
            
            take = recur2(index+2,arr)+arr[index]
            nottake = recur2(index+1,arr)
            
            dp2[index] = max(take, nottake)
            
            return dp2[index]
        
        start=recur(0,temp1)
        end=recur2(0,temp2)
        
        return max(start,end)