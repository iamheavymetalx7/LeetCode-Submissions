class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)

        gcd_ = math.gcd(n,m)
        if s+t!=t+s:
            return ""

        for i in range(gcd_):
            if s[i]==t[i]:
                continue
            else:
                return ("")

        return s[:gcd_]