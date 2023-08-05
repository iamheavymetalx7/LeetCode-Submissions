class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        prefix = [0]*(n)
        suffix =[0]*(n)
        
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        suffix[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]+nums[i]
        
        print(prefix)
        print(suffix)

        idx = 0
        mini=int(1e18)
        for i in range(n):
            if i!=n-1:
                val1,val2 = prefix[i]//(i+1), suffix[i+1]//(n-i-1)
                
            else:
                val1=prefix[-1]//n
                val2=0
            if mini>abs(val1-val2):
                mini = abs(val1-val2)
                idx = i
        return idx
                
        