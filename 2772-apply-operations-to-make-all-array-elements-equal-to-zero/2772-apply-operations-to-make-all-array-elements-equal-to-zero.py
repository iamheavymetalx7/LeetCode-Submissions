class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        n=len(nums)
        
        pref_sum =0
        arr =[0]*(n)
        
        for j in range(n):
            pref_sum+=arr[j]
            nums[j]+=pref_sum
            
            if nums[j]<0:
                return False
            if nums[j]==0:
                continue
            if j+k>n:
                return False
            
            pref_sum-=nums[j]
            if j+k<n:
                arr[j+k] += nums[j]
        # print(arr)
        return True