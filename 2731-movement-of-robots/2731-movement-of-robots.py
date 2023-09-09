class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i]=="L":
                nums[i]-=d
            else:
                nums[i]+=d
        
        MOD = int(1e9)+7
        nums.sort()
        
        
        pref = nums.copy()
        
        for i in range(1,n):
            pref[i]+=pref[i-1]
        
        # print(pref)
        ans =0
        
        for i in range(1,n):
            ans += i*nums[i]-pref[i-1]
            ans %= MOD
        return ans