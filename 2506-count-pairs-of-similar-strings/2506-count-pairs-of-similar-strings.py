class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt=0
        n=len(words)
        
        for i in range(n):
            ele=words[i]
            cf1=Counter(ele)
            
            a=sorted([key for key in cf1.keys()])
            for j in range(i+1,n):
                cf2 = Counter(words[j])
                
                b= sorted([key for key in cf2.keys()])
                
                # print(a,b,i,j)
                
                if a==b:
                    cnt+=1
        return cnt
                
        