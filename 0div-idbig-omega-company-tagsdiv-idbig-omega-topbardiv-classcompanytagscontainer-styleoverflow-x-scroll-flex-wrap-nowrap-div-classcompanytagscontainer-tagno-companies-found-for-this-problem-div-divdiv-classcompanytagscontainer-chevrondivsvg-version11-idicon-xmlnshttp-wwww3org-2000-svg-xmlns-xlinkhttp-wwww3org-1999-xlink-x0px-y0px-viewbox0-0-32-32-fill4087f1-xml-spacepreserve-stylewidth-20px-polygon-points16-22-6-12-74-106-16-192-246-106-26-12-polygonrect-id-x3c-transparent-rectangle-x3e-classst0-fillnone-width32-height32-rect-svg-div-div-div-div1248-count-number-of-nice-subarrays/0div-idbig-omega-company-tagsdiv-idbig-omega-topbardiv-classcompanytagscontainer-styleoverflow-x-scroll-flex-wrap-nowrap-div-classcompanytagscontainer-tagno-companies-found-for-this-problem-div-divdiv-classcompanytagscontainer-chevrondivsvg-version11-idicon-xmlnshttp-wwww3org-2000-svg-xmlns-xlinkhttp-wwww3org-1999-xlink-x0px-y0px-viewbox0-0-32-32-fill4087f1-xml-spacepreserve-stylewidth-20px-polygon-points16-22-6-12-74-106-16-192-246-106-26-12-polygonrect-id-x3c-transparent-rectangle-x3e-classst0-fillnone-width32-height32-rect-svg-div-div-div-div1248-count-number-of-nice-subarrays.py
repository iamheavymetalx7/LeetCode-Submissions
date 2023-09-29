class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def atmostK(cnt):
            l=0
            val =0
            
            for r in range(n):
                
                if nums[r]%2==1:
                    cnt-=1
                
                while cnt<0 and l<=r:
                    if nums[l]%2==1:
                        cnt+=1
                    l+=1
                val+=(r-l+1)
            return val
        
        val1 = atmostK(k)
        val2 = atmostK(k-1)
        
        return val1-val2