'''
https://leetcode.com/problems/number-of-beautiful-partitions/discuss/2844770/C%2B%2B-or-Classic-Partition-DP-or-Memoization-or-O(n*k)

https://leetcode.com/problems/number-of-beautiful-partitions/discuss/2833096/Python-Top-down-after-a-bunch-of-TLE-finally-works

https://leetcode.com/problems/number-of-beautiful-partitions/discuss/2832460/Python-Top-down-O(NK)-Solution-with-comparison.:

No need to take for loop, since We ONLY need to check the head of the subslice and the tail of the subslice. In that case, we don't need to define subslices by loop since we don't need to check the whole substring.
'''
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        
        n =len(s)
        primes =set(["2","3","5","7"])
        MOD = 10**9+7
        
        def isPrime(num):
            return num in primes
        
        if not isPrime(s[0]):
            return 0
        
        if isPrime(s[-1]):
            return 0
        
        @cache
        def recur(idx,k):
            if idx==n-1 and k==1:
                return 1
            if idx>=n-1 or k==0:
                return 0
            
            nottake = recur(idx+1,k)
            
            take =0
            if not isPrime(s[idx]) and isPrime(s[idx+1]):
                take = recur(idx+minLength,k-1)
            
            ans = (take+nottake)%MOD
            
            return ans
        
        return recur(minLength-1,k)
    
                
        