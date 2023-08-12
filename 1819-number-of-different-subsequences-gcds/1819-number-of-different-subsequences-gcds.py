'''
The key is, if there is an array of numbers all with factor F1, and their GCD G1 is larger than F1, then the GCD of any subsequence of them will be at least G1, F1 will not be reached.
'''

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        res =0
        all_nums = set(nums)
        
        for i in range(1,2*10**5+1):
            current_gcd = None
            for k in range(i,2*10**5+1,i):
                if k in all_nums:
                    current_gcd = k if current_gcd is None else gcd(current_gcd,k)
                    if current_gcd==i:
                        res+=1
                        break
        return res
                    
        
        