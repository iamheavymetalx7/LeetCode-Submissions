class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2,min(m-1,n-1))