class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        
        print(banned)
        
        summ=0
        cnt=0
        
        for num in range(1,n+1):
            if num in banned:
                continue
            else:
                summ+=num
                print(summ)
                if summ<=maxSum:
                    cnt+=1
        return cnt
            
        