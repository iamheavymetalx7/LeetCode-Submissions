class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        
        def isCoprime(x,y):
            
            val = math.gcd(x,y)
            if val>1:
                return False
            return True
        
        cnt =0
        for i in range(n):
            for j in range(i+1,n):
                val1 = int(str(nums[i])[0])
                val2 = nums[j]%10
                if isCoprime(val1,val2):
                    # print(nums[i],nums[j])
                    cnt+=1
        return cnt
                