class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        arr=[0]*(31)
        
        left = 0
        
        ans=0
        n =len(nums)
        
        for right in range(n):
            n = nums[right]
            
            # print(right,"rr")
            
            for i in range(31):
                if n&(1<<i) and not arr[i]:
                    arr[i]=1
                elif arr[i] and n&(1<<i):
                    while arr[i]!=0:
                        for j in range(31):
                            if nums[left]&(1<<j):
                                arr[j]-=1
                        left+=1
                    arr[i]=1                    
            ans = max(right-left+1,ans)
            
        return ans
            
            