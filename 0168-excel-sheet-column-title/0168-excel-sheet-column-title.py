class Solution:
    def convertToTitle(self, colNum: int) -> str:
        ans =""
        while colNum:
            colNum-=1
            
            ans = ans+chr((colNum)%26+ord('A'))
            colNum //=26
        
                
                
        ans=ans[::-1]
        return ans