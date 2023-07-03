class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n=len(s)
        cnt=0
                    
        if len(s)!=len(goal):
            return False
           
        

        arr=[]
        
        seen=set()
        
        for i in range(n):
            if s[i]!=goal[i]:
                arr.append(i)
                cnt+=1
            seen.add(s[i])
            
        print(cnt)
        if cnt>2:return False
        
        if cnt==2:
            return s[arr[0]]==goal[arr[1]] and goal[arr[0]]==s[arr[1]]
        
        if cnt==1:
            return False
        
        
        
        return len(seen)<len(s)
        