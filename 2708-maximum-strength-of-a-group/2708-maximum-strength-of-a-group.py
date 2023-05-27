class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        neg=[]
        pos=[]
        
        if len(nums)==1:
            return nums[0]
        
        for i in range(len(nums)):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        pos.sort(reverse=True)
        neg.sort()
        
        if nums==[0]*len(nums):
            return 0
        
        
        
        
        
        
        
        print(pos,neg)
        ans=0
        
        for i in range(1,len(nums)+1):
            for x in range(0,(i+1)//2+1):
                
                fir=x
                sec=i-x
                # print(i,fir,sec)
                prod=1
                for j in range(min(fir, len(pos))):
                    prod*=pos[j]
                for k in range(min(sec,len(neg))):
                    prod*=neg[k]
                ans=max(ans,prod)
                prod=1
                for j in range(min(fir, len(neg))):
                    prod*=neg[j]
                for k in range(min(sec, len(pos))):
                    prod*=pos[k]
                ans=max(ans,prod)
        return ans