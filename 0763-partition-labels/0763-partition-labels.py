class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i=0
        a=[]
        n=len(s)
        while i<n:
            idx =  s.rfind(s[i])
            j=i
            while j<idx:
                idx=max(idx,s.rfind(s[j]))
                j+=1

            a.append(idx-i+1)

            i=idx+1
        return a

                