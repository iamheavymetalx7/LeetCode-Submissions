class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 1000000007
        
        @cache
        def dp(idx: int, first: int, second: int, sz: int) -> int:
            if sz == 5:
                return 1
            if idx == len(s):
                return 0
            res = dp(idx + 1, first, second, sz)
            if sz == 0:
                res = (res + dp(idx + 1, (ord(s[idx]) - ord('0')), second, sz + 1)) % MOD
            elif sz == 1:
                res = (res + dp(idx + 1, first, (ord(s[idx]) - ord('0')), sz + 1)) % MOD
            elif sz == 2:
                res = (res + dp(idx + 1, first, second, sz + 1)) % MOD
            elif sz == 3:
                if ord(s[idx]) - ord('0') == second:
                    res = (res + dp(idx + 1, first, second, sz + 1)) % MOD
            elif sz == 4:
                if ord(s[idx]) - ord('0') == first:
                    res = (res + dp(idx + 1, first, second, sz + 1)) % MOD
            return res
        
        return dp(0, 10, 10, 0)