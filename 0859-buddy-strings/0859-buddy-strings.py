class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n=len(s)
        diff1=-1
        diff2=-1
            
        if len(s)!=len(goal):
            return False
        
        seen=set()
        
        for i in range(n):
            if s[i]!=goal[i]:
                if diff1==-1:
                    diff1=i
                elif diff2==-1:
                    diff2=i
                else:
                    return False
            seen.add(s[i])
        
        if diff1!=-1 and diff2!=-1:
            return s[diff1]==goal[diff2] and goal[diff1]==s[diff2]
        
        if diff1!=-1:
            return False
        
        return len(seen)<len(s)
    
        
            