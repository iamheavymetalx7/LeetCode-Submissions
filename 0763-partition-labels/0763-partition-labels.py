class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i=0
        a=[]
        n=len(s)
        dic=defaultdict(int)
        for i in range(n):
            dic[s[i]]=i
        
            
        prev=-1
        maxi=0
            
        
        for i in range(n):

            maxi= max(maxi, dic[s[i]])

            if i==maxi:
                a.append(maxi-prev)
                prev=maxi
        return a
            
                