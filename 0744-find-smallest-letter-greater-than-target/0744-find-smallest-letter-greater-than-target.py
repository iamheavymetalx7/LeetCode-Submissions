class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

                
        
        n=len(letters)
        
        arr = [ord(x) for x in letters]
        tgt = ord(target)
        
        # print(arr)
        # print(tgt)

        l,r=-1,n
            
        while r>l+1:
            m=(l+r)//2
            
            if arr[m]>tgt:
                r=m
            else:
                l=m
                
                
        ans = (r)%n
        print(ans)
        
        return chr(arr[ans])
        
        