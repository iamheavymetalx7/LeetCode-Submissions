class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        i=1
        j=0
        cnt=0
        while j<len(nums):
            if i==nums[j]:
                i+=1
                j+=1
            else:
                cnt+=1
                if cnt==k:
                    return i
                i+=1
        print(i)
        for j in range(k-cnt-1):
            i+=1
            
        return i
        
            
            
                
        