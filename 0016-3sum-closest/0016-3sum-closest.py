class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff=10**8
        
        ans=0
        
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if target == summ:
                    return summ
                elif summ>target:
                    k-=1
                else:
                    j+=1
                
                if abs(summ-target) < min_diff:
                    ans=summ
                    min_diff = abs(summ-target)
        return ans
        
        