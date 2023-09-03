class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dq = deque()
        dq.append(0)
        n=len(nums)
        
        for i in range(1,n):
            nums[i] = nums[dq[0]]+nums[i]
            
            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            if i-dq[0]>=k:
                dq.popleft()
        
        return nums[-1]