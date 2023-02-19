class Solution:
    def minOperations(self, n: int) -> int:
        # n<=10**5
        print(bin(n)[2:])
        left=0
        right=2**17+1
        mini=10**5
        for i in range(left, right):
            cnt = bin(i)[2:].count("1")
            diff = bin(n-i)[2:].count("1")
            
            mini=min(cnt+diff,mini)
        return mini