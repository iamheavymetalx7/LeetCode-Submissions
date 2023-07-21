class Solution:
    def removeDigit(self, n: str, d: str) -> str:
        ans = 0
        ll = len(n)
        for i in range(ll):
            if n[i]==d:
                l,r ="",""
                if i-1>=0:
                    l=n[:i]
                if i+1<ll:
                    r=n[i+1:]
                s=l+r
                ans=max(ans,int(s))
            else:
                continue
        
        return (str(ans))