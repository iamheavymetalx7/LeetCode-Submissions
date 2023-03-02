class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ## uses only constant extra space
        ## modifying the input array
        
        n=len(chars)
        
        i=0
        j=0
        curr = chars[0]
        cnt=0
        while i<n:
            if chars[i]==curr:
                i+=1
                cnt+=1
            else: 
                chars[j]=curr
                j+=1
                if cnt>1:
                    count_ = str(cnt)
                    for c in count_:
                        chars[j] = c
                        j+=1
                
                curr = chars[i]
                cnt=0
                
        if i==n:
            chars[j]=curr
            j+=1
            if cnt>1:
                count_ = str(cnt)
                for c in count_:
                    chars[j] = c

                    j+=1
        return j
                
            
            
            
        