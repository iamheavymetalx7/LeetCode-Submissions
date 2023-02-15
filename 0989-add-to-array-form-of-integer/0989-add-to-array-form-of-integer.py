class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        nums=""
        for n in num:
            nums+=str(n)
        new_num=int(nums)+k
        
        nn=[]
        while new_num:
            # print(new_num)
            nn.append(new_num%10)
            new_num//=10
            
        return nn[::-1]
        