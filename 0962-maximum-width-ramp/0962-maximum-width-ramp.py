class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr=[]
        
        for i,el in enumerate(nums):
            arr.append([el,i])
        
        n=len(nums)
        
        b=sorted(nums, reverse=True)
        
        flag=True
        # print([nums[0] for _ in range(n)])
        
        if [nums[0] for _ in range(n)]==nums:
            flag=False
        
        # print(flag,b,nums)
            
        if b==nums and flag and len(set(nums))==n:
            return 0
        
        arr.sort()
        # print(arr)
        
        mini = 10**9
        i=0
        cnt=1
        maxi=-1
        
        while i<n:
            # print(mini)
            if arr[i][1]<mini:
                mini= arr[i][1]
            else:
                cnt= abs(arr[i][1]-mini)
            i+=1
            maxi = max(maxi,cnt)

        
        return maxi
            
                
            