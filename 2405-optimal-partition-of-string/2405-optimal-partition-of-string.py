from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:
        dic=defaultdict(int)
        n=len(s)
        i=0
        cnt=0
        seen=set()
        while i<n:
            # print(s[i])
            if s[i] not in seen:
                seen.add(s[i])
                i+=1
            else:
                cnt+=1
                seen=set()
                seen.add(s[i])
                i+=1
        return cnt+1
            
            
            
        