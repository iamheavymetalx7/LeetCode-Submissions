'''
https://leetcode.com/problems/longest-happy-string/discuss/874072/Python-Greedy-algorithm

Idea: take the max heap, then use the element with most frequency and use it twice if available otherwise use once

Now take the second most frequent digit and we will use it only once, this is because we want to maximize the string length, if "max freq" elt is present more, we are reducing the size if we use "second max" twice.

then make use of heap structure to push the updated cnt left for each element
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap =[]
        if a:
            heappush(heap,[-a,"a"])
        if b:
            heappush(heap,[-b,"b"])
        if c:
            heappush(heap,[-c,"c"])
        
        ans =[]
        print(heap)
        while heap:
            cnt,ele = heappop(heap)
            if not ans or len(ans)>=2 and ans[-2]!=ele or ans[-1]!=ele :
                if abs(cnt)>=2:
                    ans+=[ele,ele]
                    if cnt+2:
                        heappush(heap,[cnt+2,ele])
                elif abs(cnt)>=1:
                    ans+=[ele]
                    if cnt+1:
                        heappush(heap,[cnt+1,ele])                
                
            else:
                if not heap:
                    continue
                cnt2,ele2 = heappop(heap)

                if abs(cnt2)>=1:
                    ans+=[ele2]
                    if cnt2+1:
                        heappush(heap,[cnt2+1,ele2])
                heappush(heap,[cnt,ele])
        return ''.join(ans)
                