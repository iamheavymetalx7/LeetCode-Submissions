from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        start,end=0,0
        
        dic=defaultdict(int)
        cnt=0
        n=len(fruits)
        
        for right in range(n):
            if fruits[right] in dic:
                dic[fruits[right]]+=1
            else:
                dic[fruits[right]]=1
                cnt+=1
            
            while cnt>2:
                dic[fruits[left]]-=1
                
                if dic[fruits[left]]==0:
                    cnt-=1
                    del dic[fruits[left]]
                
                left+=1
            
            if right-left+1>end-start+1:
                    start=left
                    end=right
        
        return end-start+1
                
                