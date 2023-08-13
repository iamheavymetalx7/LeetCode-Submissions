class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        idx=0
        n=len(nums)
        for i in range(n):
            if nums[i]==k:
                idx = i
                nums[i]=0
            elif nums[i]<k:
                nums[i]=-1
            elif nums[i]>k:
                nums[i]=1
        
        # print(nums)
        dic = defaultdict(int)
        dic[0]+=1
        summ=0
        for j in range(idx+1,n):
            summ+=nums[j]
            dic[summ]+=1
        
    
        backsum = 0
        
        res=dic[0]+dic[1]
        
        for i in range(idx-1,-1,-1):
            backsum += nums[i]
            res+= dic[-backsum]+dic[1-backsum]
        
        return res
            
            
            