class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

                
        
        n=len(letters)
        
        arr = [ord(x) for x in letters]
        tgt = ord(target)
        
        # print(arr)
        # print(tgt)

        l,r=0,n-1
            
        while l<=r:
            m=(l+r)//2
            
            # print(l,r,m)
                        
            if tgt<arr[m]:
                r=m-1
            else:
                l=m+1
                
                
        ans = (l)%n
        print(ans)
        
        return chr(arr[ans])
        
        